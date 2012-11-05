import unittest
import TextLogView
import Collection
import Event

class TestTextLogView(unittest.TestCase):
  def runTest(self):
    self.collection = Collection.Collection()
    self.textLV = TextLogView.TextLogView(self.collection)
    self.textLV.notify( Event.Event() )
    self.textLV.log( "Testing..." )
