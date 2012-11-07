import unittest
import Collection as col
import TaskScheduler as ts

class TestTaskScheduler(unittest.TestCase):
  def runTest(self):
    t = ts.TaskScheduler( col.Collection() )
    self.assertIs(t.getQueueIndex( 0.00 ), 0)
    t.addTask("Task 0")
    t.addTask("Task 1",1.00)
    t.addTask("Task 2",2.00)

    self.assertIs(t.getQueueIndex( -1.00 ), 0)
    self.assertIs(t.getQueueIndex( 5.00 ), len(t))
    self.assertIs( len( t ), 3 )
    
    print() 
    print(t.getTask())
    print(t.getTask())
    print(t.getTask())

 
    
