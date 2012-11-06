import Event
import Collection
import InputController
import unittest

class TestInputController(unittest.TestCase):
  class Screen:
    def getch(self):
      return True

  def runTest(self):
    coll = Collection.Collection()
    
    ev = Event.Event()
    inputController = InputController.InputController(self.Screen(), coll)

    coll.add(inputController)
    coll.notify( ev )
