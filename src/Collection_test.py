import Model
import Events
import Collections
import unittest

class TestCollection(unittest.TestCase):
  def runTest(self):
    self.coll = Collections.Collection()
    self.m = Model.Model("0")
    self.ev = Events.Event()

    self.coll.add(self.m)
    self.assertIs(len(self.coll),1)
    self.coll.remove(self.m)
    self.assertIs(len(self.coll),0)
    self.coll.notify( self.ev )
