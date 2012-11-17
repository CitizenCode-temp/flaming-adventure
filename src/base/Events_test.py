import Events
import unittest

class TestEvents(unittest.TestCase):
  def testEvent(self):
    self.event = Events.Event()
    self.event.getName() 

  def testStepEvent(self):
    self.event = Events.StepEvent()
    self.assertIs(self.event.getName(), "StepEvent") 

  def testQuitEvent(self):
    self.event = Events.QuitEvent()
    self.assertIs(self.event.getName(), "QuitEvent") 

  def testInputEvent(self):
    self.event = Events.InputEvent("test string")
    self.assertIs(self.event.getName(), "InputEvent") 
    self.assertIs(self.event.getInputStr(), "test string") 

  def testLogMsgEvent(self):
    self.event = Events.LogMsgEvent("test string")
    self.assertIs(self.event.getName(), "LogMsgEvent") 
    self.assertIs(self.event.getMsg(), "test string") 

