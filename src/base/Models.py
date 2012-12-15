import Events
import Collections

class Model:
  def __init__(self,_id):
    self._id = _id 

  def notify( self, event ):
    return True 

  def getId(self):
    return self._id

class Map(Model):
  def __init__(self, _id):
    self._id = _id
    self.size = 10
    self.mapArray = self.makeMapArray(self.size)

  def makeMapArray(self, size):
    mapArray = []
    for x in range(size):
      mapColumn = []
      for y in range(size):
        mapColumn.append( Collections.MapSector("msector-" + str(x) + "-" + str(y)) )
      mapArray.append(mapColumn)

    return mapArray

  def checkIfContains(self, x, y):
    if (x >= 0 and x < self.getWidth() and y >=0 and y < self.getHeight()):
      return True
    else:
      return False

  def getMapArray(self):
    return self.mapArray

  def getWidth(self):
    return self.size

  def getHeight(self):
    return self.size

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
    if isinstance(event, Events.MoveEvent):
      self.mvPlayer( event )

    return True

  def mvPlayer(self, mvEvent):
    x = self.x + mvEvent.getDx()
    y = self.y + mvEvent.getDy()
    if( self.appCollection.getMapCollection().getCurrentMap().checkIfContains(x,y) ):
      self.x = x
      self.y = y
      self.appCollection.notify( Events.LogMsgEvent("You moved!") )

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
