"""
  Collection

    A collection provides an abstraction for working with sets of other objects.
  One important role they play is forwarding Events to their members via the
  notify function.
"""
import adv
import FAMap
import characters

class Collection:
  def __init__(self):
    self.members = []

  def __len__(self):
    return len( self.members )

  def add(self, obj):
    """
    Add an object to the collection. It must not already be a member of the
    collection and must implement a notify method.
    """
    if not hasattr(obj, 'notify'):
      raise Exception(
        "Tried to add {0} with no notify method to {1}".format(
          obj,
          self
        )
      )

    if (self.members.count(obj) == 0):
      self.members.append(obj) 

  def remove(self, obj):
    self.members.remove(obj)

  def forEach(self, func):
    for m in self.members:
      func(m)

  def notify(self, event):
    for m in self.members:
      m.notify(event)

class AppCollection(Collection):

  def init_resources(self):
    self.player = characters.Player("player-0")
    self.mapCollection = MapCollection(self.player) 
  
  def notifyMaps(self, event):
    self.mapCollection.notify(event)

  def setAppView(self, appView):
    self.appView = appView
    self.add( appView )

  def getAppView(self):
    return self.appView

  def notifyAppView(self, event):
    self.appView.notify( event )

  def getPlayer(self):
    return self.player

  def getMapCollection(self):
    return self.mapCollection

class MapCollection(Collection):
  def __init__(self, player):
    self.appCollection = adv.app.appColl
    self.mapCreator = FAMap.MapCreator(self.appCollection)
    self.members = [ self.getInitialMap( player ) ]
    self.currentMap = self.members[0]

  def getInitialMap(self, player):
    first_map = self.mapCreator.createMap("map-0")
    first_map.insertPlayer( player )
    return first_map

  def getCurrentMap(self):
    return self.currentMap
