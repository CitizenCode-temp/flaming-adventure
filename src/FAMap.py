import random

import FAModels
from sectors import MapSector, WallMapSector

def get_2d_random(
    xmax,
    ymax,
    xmin=0,
    ymin=0,
    near=None,
    near_distance=0
):
    """Generate an (x, y) coordinate tuple somewhere in the specified
    rectangle."""
    given_xmax = xmax 
    given_ymax = ymax 
    if near is not None:
        xmin = near[0]
        ymin = near[1]
        xmax = xmin + near_distance
        ymax = ymin + near_distance
        if xmax > given_xmax:
            xmax = given_xmax
        if ymax > given_ymax:
            ymax = given_ymax
    
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    return x, y

class Room:
    def __init__(self, x0, y0, xmax, ymax, room_size):
        # Upper left hand corner of the room
        self.x0 = x0
        self.y0 = y0
        # Map dimensions
        self.xmin = 0
        self.xmax = xmax
        self.ymin = 0
        self.ymax = ymax
        # Room dimensions
        self.room_size = room_size
        self.min_size = 2

        self.room = self.make_room()

    def make_room(self):
        def get_corners():
            corner1 = (self.x0, self.y0)
            corner2 = get_2d_random(self.xmax, self.ymax, near=corner1, near_distance=self.room_size)
            return corner1, corner2

        c1, c2 = get_corners()
        # c1 is guarenteed to be 'bigger' than c2
        x1, y1 = c1
        x2, y2 = c2
        # Make a zero-indexed room
        room = []
        for x in range(x2 + 1 - x1):
            room_column = []
            for y in range(y2 + 1 - y1):
                if (x in [0, x2 - x1 - 1] or y in [0, y2 - y1 - 1]):
                    room_column.append(WallMapSector("wmsector-{0}-{1}".format(x, y)))
                else:
                    room_column.append(MapSector("msector-{0}-{1}".format(x, y)))
            room.append(room_column)

        return room

    def append_to_map_array(self, map_array):
        x1 = self.x0
        x2 = self.x0 + len(self.room) - 1
        y1 = self.y0
        y2 = self.y0 + len(self.room[0]) - 1
        for x in range(x1, x2):
            for y in range(y1, y2):
                map_array[x][y] = self.room[x - x1][y - y1]

class MapCreator:
  def __init__(self):
    self.sizeX = 60
    self.sizeY = 25

  def make_impassable_areas(self, map_array):
    n = 5
    room_size = 10
    xmax = self.sizeX - 1 
    ymax = self.sizeY - 1
    for _ in range(n):
      x, y = get_2d_random(xmax, ymax)
      r = Room(x, y, xmax, ymax, room_size)
      r.append_to_map_array(map_array)

  def createMap(self, _id):
    # Create the base tile
    mapArray = self.makeMapSectorArray( self.sizeX, self.sizeY )

    # randomly generate impassable areas
    self.make_impassable_areas(mapArray)

    newMap = Map(_id, mapArray)
    return newMap

  def makeMapSectorArray(self, sizeX, sizeY):
    mapArray = []
    for x in range(sizeX):
      mapColumn = []
      for y in range(sizeY):
        mapColumn.append( MapSector("msector-" + str(x) + "-" + str(y)) )
      mapArray.append(mapColumn)

    return mapArray

class Map(FAModels.Model):
  def __init__(self, _id, mapSectorArray):
    self._id = _id
    self.mapSectorArray = mapSectorArray

  def insertPlayer(self, player):
    x = 9 
    y = 9
    ms = self.mapSectorArray[x][y]
    ms.addCharacter( player )
    player.setXY(x,y)
    player.setCurrentMap( self )

  def movePlayer(self, player, x, y):
    if not self.isPassable( x, y ):
      return player.getXY() 
    [plX, plY] = player.getXY() 
    self.mapSectorArray[plX][plY].removeCharacter( player )
    self.mapSectorArray[x][y].addCharacter( player )
    return [x, y]

  def isPassable(self, x, y):
    if not self.contains(x, y):
      return False
    return self.mapSectorArray[x][y].isPassable()

  def contains(self, x, y):
    if (x >= 0 and x < self.getWidth() and y >=0 and y < self.getHeight()):
      return True
    else:
      return False

  def getMapSectorArray(self):
    return self.mapSectorArray

  def getWidth(self):
    return len( self.mapSectorArray )

  def getHeight(self):
    return len( self.mapSectorArray[0] )
