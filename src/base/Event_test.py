import Event
import unittest

class TestEvent(unittest.TestCase):
  def runTest(self):
    self.event = Event.Event()
    self.event.getName() 
