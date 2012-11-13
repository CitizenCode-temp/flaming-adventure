import Events
import Models
import unittest

class TestModels(unittest.TestCase):
  def runTest(self):
    self.model = Model.Model("zero")
    self.model.getId()
    self.model.notify( Events.Event() ) 

  
