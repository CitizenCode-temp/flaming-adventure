"""
  Collection

    A collection provides an abstraction for working with sets of other objects.
  One important role they play is forwarding Events to their members via the
  notify function.
"""
import adv
import FAMap

class Collection:
    """
    A Collection is a list of objects that is unique, and also implements a
    notify method. This allows us to pass messages to game resources/collection
    members.
    """
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

    def notify(self, event):
      for m in self.members:
        m.notify(event)

class AppCollection(Collection):
    """
    A singleton of this class holds all the game resources. This facilitates
    a system-wide message passing point as well as shortcuts to other sets
    of object -- maps, views, the player, etc...
    """
  
    def init_map_collection(self):
        self.mapCollection = MapCollection(self.player) 
  
    def set_player(self,p):
        self.player = p
  
    def get_player(self):
        return self.player
  
    def get_map_collection(self):
        return self.mapCollection
  
    def notify(self, event):
        # Notify the views
        adv.app.app_view.notify(event)

        # Notify other resources
        for m in self.members:
            m.notify(event)


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
