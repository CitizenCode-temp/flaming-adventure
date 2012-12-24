import FAParser
import FAEvents

class FAInputController:
  def __init__(self, appCollection):
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.parser = FAParser.faParser(self, appCollection) 
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, FAEvents.InputEvent):
      self.parse( event.getInputStr() )

  def parse(self, cmd):
    self.cmdHistory.append(cmd)
    self.parser.parse(cmd)
