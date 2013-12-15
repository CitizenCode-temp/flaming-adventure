import random

import FAModels
import FACollections 

class MapCreator:
  def __init__(self):
    self.sizeX = 80
    self.sizeY = 25

  def make_impassable_areas(self, map_array):
    n = 20
    def gen_2d_randoms():
      for _ in range(n):
        yield (
          random.randint(0, self.sizeX - 1),
          random.randint(0, self.sizeY - 1)
        )
                
    for x, y in gen_2d_randoms():
        map_array[x][y] = WallMapSector("wmsector-{0}-{1}".format(x, y))

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

class MapSector(FAModels.Model):
  def __init__(self, _id):
    self._id = _id
    self.characters = FACollections.Collection() 
    self.items = FACollections.Collection() 
    self.setSectorAttributes()

  def setSectorAttributes(self):
    self.strRep = "."
    self.passable = True

  def getStrRep(self):
    return self.strRep

  def isPassable(self):
    return self.passable

  def removeCharacter(self, charObj):
    self.characters.remove(charObj)

  def addCharacter(self, charObj):
    self.characters.add(charObj)

class WallMapSector(MapSector):
  def setSectorAttributes(self):
    self.strRep = "="
    self.passable = False
