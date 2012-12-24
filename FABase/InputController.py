import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import FAParsers.faParser as faParser
import Events

class InputController:
  def __init__(self, appCollection):
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.parser = faParser.faParser(self, appCollection) 
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, Events.InputEvent):
      self.parse( event.getInputStr() )

  def parse(self, cmd):
    self.cmdHistory.append(cmd)
    self.parser.parse(cmd)
