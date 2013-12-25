import os
import sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import unittest
import FAEvents
import FAViews
import FAModels
import FACollections

class FakeScreen:
  def refresh(self):
    return True

class TestModels(unittest.TestCase):
  def testView(self):
    self.model = FAModels.Model("id-0")
    self.screen = FakeScreen()
    self.collection = FACollections.Collection()
    self.v = FAViews.View( self.model, self.screen, self.collection )
    self.assertTrue( self.v.refresh() )
    self.assertTrue( self.v.notify( FAEvents.StepEvent() ) )
