import adv
import FAEvents

class Model:
  def __init__(self,_id):
    self._id = _id 

  def notify( self, event ):
    return True 

  def getId(self):
    return self._id

class NPC(Model):
  def __init__(self, _id, char='m'):
    self._id = _id
    self.char = char
    self.appCollection = adv.app.appColl
    self.name = "Fluffy the vampire slayer (NPC)"
    self.maxHealth = 10.0
    self.health = 10.0
    self.level = 0
    self.x = 0
    self.y = 0
    self.is_passable = False
    self.currentMap = None

  def get_passable(self):
    return self.is_passable

  def get_char(self):
    return self.char

  def setCurrentMap(self, aMap):
    self.currentMap = aMap

  def getCurrentMap(self):
    return self.currentMap

  def getMaxHealth(self):
    return self.maxHealth

  def getLevel(self):
    return self.level

  def setAppCollection(self, appCollection):
    self.appCollection = appCollection

  def notify(self, event):
    return True

  def move(self, mvEvent):
    x = self.x + mvEvent.getDx()
    y = self.y + mvEvent.getDy()
    [self.x, self.y] = self.appCollection.getMapCollection().getCurrentMap().move_npc(self, x, y)

  def getName(self):
    return self.name

  def setName(self, name):
    self.name = name

  def getHealth(self):
    return self.health

  def setHealth(self, health):
    self.health = health

  def getXY(self):
    return [self.x, self.y]

  def setXY(self, x, y):
    self.x = x
    self.y = y

  def getDescription(self):
    descrip = self.name + "(NPC) Lvl " + str(self.getLevel()) + " | HP " + str( self.getHealth() ) + "/" + str( self.getMaxHealth() ) + "\n\n"
    descrip += "A nondescript townsperson"
    return descrip

class Player(NPC):
  def __init__(self, _id):
    self._id = _id
    self.appCollection = adv.app.appColl
    self.name = "Flarg"
    self.maxHealth = 10.0
    self.health = 10.0
    self.level = 0
    self.x = 0
    self.y = 0
    self.is_passable = False
    self.currentMap = None

  def notify(self, event):
    if isinstance(event, FAEvents.MoveEvent):
      self.mvPlayer( event )
    return True

  def mvPlayer(self, mvEvent):
    x = self.x + mvEvent.getDx()
    y = self.y + mvEvent.getDy()
    [self.x, self.y] = self.appCollection.getMapCollection().getCurrentMap().movePlayer(self, x, y)

  def getDescription(self):
    playerStr = self.name + " Lvl " + str(self.getLevel()) + " | HP " + str( self.getHealth() ) + "/" + str( self.getMaxHealth() ) + "\n\n"
    playerStr += "A long description here, will tell the tale of adventures past. The story of scars, tired eyes, and hunger."
    return playerStr
