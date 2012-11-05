import EventManager
import Event
import Model
import unittest

class TestEventManager(unittest.TestCase):
  def runTest(self):
    self.ev_mgr = EventManager.EventManager()
    self.model = Model.Model()
    self.event = Event.Event()

    self.ev_mgr.registerListener( self.model )
    self.ev_mgr.notify( self.event )
    self.ev_mgr.unregisterListener( self.model ) 

  
