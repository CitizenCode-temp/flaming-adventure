"""
  Collection

    A collection provides an abstraction for working with sets of other objects.
  One important role they play is forwarding Events to their members via the
  notify function.
"""
import FAMap
import FAModels

class Collection:
  def __init__(self):
    self.members = []

  def __len__(self):
    return len( self.members )

  def add(self, obj):
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
  def __init__(self):
    self.members = []
    self.player = FAModels.Player("player-0", self)
    self.add( self.player )
    self.mapCollection = MapCollection(self, self.player) 
  
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
  def __init__(self, appCollection, player):
    self.appCollection = appCollection
    self.mapCreator = FAMap.MapCreator()
    self.members = [ self.getInitialMap( player ) ]
    self.currentMap = self.members[0]

  def getInitialMap(self, player):
    firstMap = self.mapCreator.createMap("map-0")
    firstMap.insertPlayer( player )
    return firstMap

  def getCurrentMap(self):
    return self.currentMap
