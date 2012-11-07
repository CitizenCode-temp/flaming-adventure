import Model
import Events
import Collection
import unittest

class TestCollection(unittest.TestCase):
  def runTest(self):
    self.coll = Collection.Collection()
    self.m = Model.Model("0")
    self.ev = Events.Event()

    self.coll.add(self.m)
    self.assertIs(self.coll.getLength(),1)
    self.coll.remove(self.m)
    self.assertIs(len(self.coll.members),0)
    self.coll.notify( self.ev )
