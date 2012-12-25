import FAEvents
import FACollections

class Model:
  def __init__(self,_id):
    self._id = _id 

  def notify( self, event ):
    return True 

  def getId(self):
    return self._id

class Player(Model):
  def __init__(self, _id):
      self._id = _id
      self.name = "Flarg"
      self.maxHealth = 10.0
      self.health = 10.0
      self.level = 0
      self.x = 0
      self.y = 0

  def getMaxHealth(self):
    return self.maxHealth

  def getHealth(self):
    return self.health

  def getLevel(self):
    return self.level

  def setAppCollection(self, appCollection):
    self.appCollection = appCollection

  def notify(self, event):
    if isinstance(event, FAEvents.MoveEvent):
      self.mvPlayer( event )
    return True

  def mvPlayer(self, mvEvent):
    x = self.x + mvEvent.getDx()
    y = self.y + mvEvent.getDy()
    if( self.appCollection.getMapCollection().getCurrentMap().checkIfContains(x,y) ):
      self.x = x
      self.y = y

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
