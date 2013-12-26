import adv
import FAEvents

class Model(object):
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
    self.appCollection.add(self)
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

  def move_x_y(self, x, y):
    [self.x, self.y] = self.appCollection.getMapCollection().getCurrentMap().move_char(self, x, y)

  def move(self, mv_event):
    x = self.x + mv_event.getDx()
    y = self.y + mv_event.getDy()
    self.move_x_y(x, y)

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
    descrip = self.name + " Lvl " + str(self.getLevel()) + " | HP " + str( self.getHealth() ) + "/" + str( self.getMaxHealth() ) + "\n\n"
    return descrip


class Monster(NPC):
    def __init__(self, _id, char='m'):
        super(Monster, self).__init__(_id, char)
        self.name = "Evil Crud (Monster)"

    def notify(self, event):
        if isinstance(event, FAEvents.StepEvent):
            self.do_turn()

    def do_turn(self):
        self.hunt_player()

    def hunt_player(self):
        """
        Step one tile in the player's direction
        """
        def get_d(z0, z1):
            diff = z1 - z0
            if diff == 0:
                return 0
            else:
                return diff/abs(diff)

        (cx, cy) = self.x, self.y
        (px, py) = self.appCollection.getPlayer().getXY()
        (dx, dy) = get_d(cx, px), get_d(cy, py)
        self.move_x_y(cx + dx, cy + dy)


class Player(NPC):
  def __init__(self, _id):
    self._id = _id
    self.appCollection = adv.app.appColl
    self.appCollection.add( self )
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
      self.move( event )
    return True

  def getDescription(self):
    desc = self.name + " Lvl " + str(self.getLevel()) + " | HP " + str( self.getHealth() ) + "/" + str( self.getMaxHealth() ) + "\n\n"
    desc += "A long description here, will tell the tale of adventures past. The story of scars, tired eyes, and hunger."
    return desc
