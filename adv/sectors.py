import model
import FACollections

class MapSector(model.Model):
  def __init__(self, _id):
    self._id = _id
    self.characters = []
    self.items = FACollections.Collection() 
    self.setSectorAttributes()

  def setSectorAttributes(self):
    self.strRep = "."
    self.passable = True

  def getStrRep(self):
    return self.strRep

  def is_passable(self):
    p = self.passable
    if p:
      for c in self.characters:
        if not c.get_passable():
          p = False
    return p

  def removeCharacter(self, charObj):
    self.characters.remove(charObj)

  def addCharacter(self, charObj):
    self.characters.append(charObj)

  def is_empty(self):
    return len(self.characters) == 0

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
