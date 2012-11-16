import Events

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
        mapColumn.append( MapSector("msector-" + str(x) + "-" + str(y)) )
      mapArray.append(mapColumn)

    return mapArray

  def getMapArray(self):
    return self.mapArray

  def getWidth(self):
    return self.size

  def getHeight(self):
    return self.size

class MapSector(Model):
  def __init__(self, _id):
    self._id = _id
    self.strRep = "."

  def getStrRep(self):
    return self.strRep


class Player(Model):
  def __init__(self, _id):
      self._id = _id
      self.name = "Flarg"
      self.health = 10.0
      self.x = 0
      self.y = 0

  def setAppCollection(self, appCollection):
    self.appCollection = appCollection

  def notify(self, event):
    if isinstance(event, Events.MoveEvent):
      self.mvPlayer( event )

    return True

  def mvPlayer(self, mvEvent):
    self.x = self.x + mvEvent.getDx()
    self.y = self.y + mvEvent.getDy()

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
