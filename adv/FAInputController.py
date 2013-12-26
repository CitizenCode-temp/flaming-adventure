import adv
import FAParser
import events

class InputController:
  def __init__(self, appView):
    self.appCollection = adv.app.appColl
    self.appView = appView
    self.appCollection.add(self)
    self.parser = FAParser.Parser(self) 
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, events.StepEvent):
      initialChar = self.appView.getCmdLineView().getCh()
      self.parser.parseChar(initialChar)

  def getInsertModeCmd(self):
    self.appView.getStatusView().setStatusFlag('Insert Mode')
    self.appView.getStatusView().refresh()
    self.parse( self.appView.getCmdLineView().getStrCmd() )
    self.appView.getStatusView().setStatusFlag('Cmd Mode')
    self.appView.getStatusView().refresh()

  def parse(self, cmd):
    self.cmdHistory.append(cmd)
    self.parser.parse(cmd)
