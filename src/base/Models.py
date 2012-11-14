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

  def notify(self, event):
    return True

  def getStrRep(self):
    return "."

class Player(Model):
  def __init__(self, _id):
      self._id = _id
      self.name = ""
      self.health = 10

  def notify(self, event):
    return True

  def getName(self):
    return self.name

  def setName(self, name):
    self.name = name

  def getHealth(self):
    return self.name

  def setHealth(self, name):
    self.name = name
