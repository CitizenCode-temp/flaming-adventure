import FAModels
import FACollections

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
    self.strRep = "#"
    self.passable = False

class DoorMapSector(MapSector):
  def setSectorAttributes(self):
    self.strRep = "."
    self.passable = True

class DebugMapSector(MapSector):
  def setSectorAttributes(self):
    self.strRep = "?"
    self.passable = True
