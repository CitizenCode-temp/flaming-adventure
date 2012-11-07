import Events
import unittest

class TestEvents(unittest.TestCase):
  def runTest(self):
    self.event = Events.Event()
    self.event.getName() 
