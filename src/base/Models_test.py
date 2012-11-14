# Test the interface of all module classes
import Events
import Models
import unittest

class TestModels(unittest.TestCase):

  def testModel(self):
    self.model = Models.Model("model_0")
    self.model.getId()
    self.model.notify( Events.Event() ) 

  def testMap(self):
    self.mapModel = Models.Map("model_0")
    self.mapModel.getId()
    self.mapModel.notify( Events.Event() ) 
    self.mapModel.getStrRep()


  
