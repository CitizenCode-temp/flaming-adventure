import FAModels
import FAEvents
import FACollections 

class MapCreator:
  def __init__(self):
    self.sizeX = 60
    self.sizeY = 10

  def createMap(self, _id):
    # Create the base tile
    mapArray = self.makeMapSectorArray( self.sizeX, self.sizeY )
    # Make a single impassable area
    mapArray[15][4] = WallMapSector("wmsector-15-15")

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

  def checkIfContains(self, x, y):
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

class WallMapSector(MapSector):
  def setSectorAttributes(self):
    self.strRep = "="
    self.passable = False
