# Test the interface of all module classes
import Events
import Models
import unittest

class TestModels(unittest.TestCase):

  def testModel(self):
    self.model = Models.Model("model-0")
    self.model.getId()
    self.model.notify( Events.Event() ) 

  def testMap(self):
    self.mapModel = Models.Map("map-0")
    self.mapModel.getId()
    self.mapModel.makeMapeArray(5)
    self.mapModel.checkIfContains(2,2)
    self.mapModel.getMapArray()
    self.mapModel.getWidth()
    self.mapModel.getHeight()
    self.mapModel.notify( Events.Event() ) 

  def testPlayer(self):
    self.player = Models.Player("player-0")
    self.player.getId()
    self.player.notify( Events.Event() ) 
    self.player.getName()
    self.player.setName("Bill")
    self.assertIs(self.player.getName(),"Bill")
    self.player.getHealth()
    self.player.setHealth(5.00)
    self.assertIs(self.player.getHealth(),5.00)
    self.player.getMaxHealth()
    self.player.


  
