import unittest
import Collection as col
import Events
import EventScheduler as ts

class TestEventScheduler(unittest.TestCase):
  def runTest(self):
    t = ts.EventScheduler( col.Collection() )
    self.assertIs(t.getQueueIndex( 0.00 ), 0)
    ev = Events.Event()
    t.addEvent(ev)
    t.addEvent(ev,0.50)
    t.addEvent(ev,1.00)
    t.addEvent(ev,2.30)
    t.addEvent(ev,3.30)

    self.assertIs(t.getQueueIndex( -1.00 ), 0)
    self.assertIs(t.getQueueIndex( 5.00 ), len(t))
    self.assertIs( len( t ), 5 )
    print()
    print( str( t.queue ) )
    
    t.doTurn()
    self.assertIs( len( t ), 3 )
    print( str( t.queue ) )

    t.doTurn()
    self.assertIs( len( t ), 2 )
    print( str( t.queue ) )
