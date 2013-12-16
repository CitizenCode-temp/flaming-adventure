import random

import FAModels
from sectors import MapSector, WallMapSector, DoorMapSector, DebugMapSector

def get_2d_random(
    xmax,
    ymax,
    xmin=0,
    ymin=0,
    near=None,
    min_distance=0,
    max_distance=0
):
    """Generate an (x, y) coordinate tuple somewhere in the specified
    rectangle."""
    given_xmax = xmax 
    given_ymax = ymax 

    if near is not None:
        xmin = near[0] + min_distance
        ymin = near[1] + min_distance
        xmax = near[0] + max_distance
        ymax = near[1] + max_distance
        if xmax > given_xmax:
            xmax = given_xmax
        if ymax > given_ymax:
            ymax = given_ymax
        if xmin > xmax:
            xmin = xmax
        if ymin > ymax:
            ymin = ymax

    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    return x, y

class Room:
    def __init__(self, x0, y0, xmax, ymax, min_room_size, max_room_size):
        # Upper left hand corner of the room
        self.x0 = x0
        self.y0 = y0
        # Map dimensions
        self.xmin = 0
        self.xmax = xmax
        self.ymin = 0
        self.ymax = ymax
        # Room dimensions
        self.min_room_size = min_room_size
        self.max_room_size = max_room_size
        self.max_doors = 2

        self.room = self.make_room()

    def make_room(self):
        def get_corners():
            corner1 = (self.x0, self.y0)
            corner2 = get_2d_random(
                self.xmax,
                self.ymax,
                near=corner1,
                min_distance=self.min_room_size,
                max_distance=self.max_room_size
            )
            return corner1, corner2

        c1, c2 = get_corners()
        # c1 is guarenteed to be 'bigger' than c2
        x1, y1 = c1
        x2, y2 = c2
        # Make a zero-indexed room
        room = []
        for x in range(x2 - x1):
            room_column = []
            for y in range(y2 - y1):
                room_column.append(MapSector("msector-{0}-{1}".format(x, y)))
            room.append(room_column)

        walls = self.get_room_walls(room)
        for t in walls:
            x, y = t
            room[x][y] = WallMapSector("wallmsector-{0}-{1}".format(x, y))

        room = self.make_doors(room)

        return room

    def get_room_walls(self, room, no_corners=False):
        wall_sectors = []
        xmax = len(room) - 1
        ymax = len(room[0]) - 1
        for x in range(len(room)):
            for y in range(len(room[0])):
                if no_corners:
                    if (x in [0, xmax]) != (y in [0, ymax]):
                        wall_sectors.append((x, y))
                else:
                    if (x in [0, xmax]) or (y in [0, ymax]):
                        wall_sectors.append((x, y))
        return wall_sectors

    def make_doors(self, room):
        n = random.randint(1, self.max_doors)
        walls = self.get_room_walls(room, no_corners=True)
        for _ in range(n):
            x, y = random.choice(walls)
            room[x][y] = DoorMapSector("doormsector-{0}-{1}".format(x, y))
        return room

    def append_to_map_array(self, map_array):
        x1 = self.x0
        x2 = self.x0 + len(self.room)
        y1 = self.y0
        y2 = self.y0 + len(self.room[0])
        for x in range(x1, x2):
            for y in range(y1, y2):
                map_array[x][y] = self.room[x - x1][y - y1]

class MapCreator:
  def __init__(self):
    self.sizeX = 60
    self.sizeY = 25

  def make_impassable_areas(self, map_array):
    n = 5
    min_room_size = 5
    max_room_size = 10
    xmax = self.sizeX
    ymax = self.sizeY
    for _ in range(n):
      x, y = get_2d_random(xmax - 1 - min_room_size, ymax - 1 - min_room_size)
      r = Room(x, y, xmax, ymax, min_room_size, max_room_size)
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
