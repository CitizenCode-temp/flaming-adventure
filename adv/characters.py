import math
import random

import adv
from fightable import Fightable
from model import Model
import events

class NPC(Model):
  def __init__(self, _id, char='m'):
    super(NPC, self).__init__(_id, char=char)
    self._id = _id
    self.char = char
    self.appCollection = adv.app.appColl
    self.appCollection.add(self)
    self.name = "Fluffy the vampire slayer (NPC)"
    self.maxHealth = 10.0
    self.health = 10.0
    self.level = 0
    self.strength = 2
    self.defense = 1
    self.speed = 1
    self.x = 0
    self.y = 0
    self.is_passable = False
    self.currentMap = None

  def die(self):
      self.char = 'x'

  @property
  def is_dead(self):
      return self.health > 0

  def get_defense(self):
    return self.defense

  def get_speed(self):
    return self.speed

  def is_alive(self):
      return self.health > 0

  def resolve_char_contact(self, char):
    self.appCollection.notify(
      events.LogMsgEvent(
        "{0} resolving against {1}".format(
            self.name,
            char.getName()
        )

      )
    )

  def get_passable(self):
    return self.is_passable

  def get_char(self):
    return self.char

  def setCurrentMap(self, aMap):
    self.currentMap = aMap

  def getCurrentMap(self):
    return self.currentMap

  def get_max_health(self):
    return self.maxHealth

  def get_level(self):
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

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_health(self):
    return self.health

  def set_health(self, health):
    self.health = health
    if self.health <= 0:
        self.die()

  def getXY(self):
    return [self.x, self.y]

  def setXY(self, x, y):
    self.x = x
    self.y = y

  def getDescription(self):
    descrip = self.name + " Lvl " + str(self.getLevel()) + " | HP " + str( self.getHealth() ) + "/" + str( self.getMaxHealth() ) + "\n\n"
    return descrip


class Monster(NPC, Fightable):
    def __init__(self, _id, char='m'):
        super(Monster, self).__init__(_id, char=char)
        self.name = "Evil Crud (Monster)"

    def resolve_char_contact(self, char):
        self.do_combat(char)

    def notify(self, event):
        if isinstance(event, events.StepEvent):
            if self.is_alive():
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

        sensitivity = 20
        (cx, cy) = self.x, self.y

        if self.get_player_dist() <= sensitivity:
            (px, py) = self.appCollection.getPlayer().getXY()
            (dx, dy) = get_d(cx, px), get_d(cy, py)
        else:
            (dx, dy) = random.randint(-1, 1), random.randint(-1, 1)

        self.move_x_y(cx + dx, cy + dy)

    def get_player_dist(self):
        (cx, cy) = self.x, self.y
        (px, py) = self.appCollection.getPlayer().getXY()
        dist = int(math.sqrt((px - cx)**2 + (py - cy)**2))
        return dist



class Player(NPC, Fightable):
  def __init__(self, _id):
    super(Player, self).__init__(_id, char='@')
    self.name = "Flarg"

  def notify(self, event):
    if isinstance(event, events.MoveEvent):
      self.move( event )
    return True

  def getDescription(self):
    desc = self.name + " Lvl " + str(self.get_level()) + " | HP " + str( self.get_health() ) + "/" + str( self.get_max_health() ) + "\n\n"
    desc += "A long description here, will tell the tale of adventures past. The story of scars, tired eyes, and hunger."
    return desc

  def resolve_char_contact(self, char):
    self.do_combat(char)
