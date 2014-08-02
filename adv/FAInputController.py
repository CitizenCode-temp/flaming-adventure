import adv
import FAParser
import events

class InputController:
  def __init__(self, app_view):
    self.appCollection = adv.app.appColl
    self.app_view = app_view
    self.appCollection.add(self)
    self.parser = FAParser.Parser(self) 
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, events.StepEvent):
      initialChar = self.app_view.getCmdLineView().getCh()
      self.parser.parseChar(initialChar)

  def getInsertModeCmd(self):
    self.app_view.getStatusView().setStatusFlag('Insert Mode')
    self.app_view.getStatusView().refresh()
    self.parse( self.app_view.getCmdLineView().getStrCmd() )
    self.app_view.getStatusView().setStatusFlag('Cmd Mode')
    self.app_view.getStatusView().refresh()

  def parse(self, cmd):
    self.cmdHistory.append(cmd)
    self.parser.parse(cmd)
