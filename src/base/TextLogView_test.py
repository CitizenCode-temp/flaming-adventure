import unittest
import TextLogView
import EventManager
import Event

class TestTextLogView(unittest.TestCase):
  def runTest(self):
    self.evManager = EventManager.EventManager()
    self.textLV = TextLogView.TextLogView(self.evManager)
    self.textLV.notify( Event.Event() )
    self.textLV.log( "Testing..." )
