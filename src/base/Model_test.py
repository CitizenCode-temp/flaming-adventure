import Event
import Model
import unittest

class TestModel(unittest.TestCase):
  def runTest(self):
    self.model = Model.Model()
    self.model.getId()
    self.model.notify( Event.Event() ) 

  
