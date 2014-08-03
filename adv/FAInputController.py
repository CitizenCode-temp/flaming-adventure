import adv
import FAViews
import FAParser
import events

class InputController:
  def __init__(self, app_view):
    self.appCollection = adv.app.appColl
    self.appCollection.add(self)
    self.parser = FAParser.Parser(self) 
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(adv.app.app_view, FAViews.AdventureView):
        # In Adventure mode, wait for a single command from the user
        if isinstance(event, events.StepEvent):
          initialChar = adv.app.app_view.getCmdLineView().getCh()
          self.parser.parseChar(initialChar)

  def getInsertModeCmd(self):
    adv.app.app_view.getStatusView().setStatusFlag('Insert Mode')
    adv.app.app_view.getStatusView().refresh()
    self.parse( adv.app.app_view.getCmdLineView().getStrCmd() )
    adv.app.app_view.getStatusView().setStatusFlag('Cmd Mode')
    adv.app.app_view.getStatusView().refresh()

  def parse(self, cmd):
    self.cmdHistory.append(cmd)
    self.parser.parse(cmd)
