import Events
import Collections
import InputController
import unittest

class TestInputController(unittest.TestCase):
  class Screen:
    def getch(self):
      return True

  def runTest(self):
    coll = Collections.Collection()
    
    ev = Events.StepEvent()
    inputController = InputController.InputController(self.Screen(), coll)

    coll.add(inputController)
    coll.notify( ev )
