import curses
import Events

class AppView:
  def __init__(self, model, screen, appCollection):
    self.model = model
    self.height = screen.getmaxyx()[0]
    self.width = screen.getmaxyx()[1]
    self.screen = screen
    self.cmdLine = curses.newwin(3,self.width,self.height - 3,0) 
    self.cmdLine.scrollok(True)
    self.appCollection = appCollection
    self.appCollection.add(self)

  def refresh(self):
    self.cmdLine.scroll(-1)
    self.screen.refresh()

  def notify(self, event):
    if isinstance(event, Events.StepEvent):
      self.refresh()

  def getCmdLineView(self):
    return self.cmdLine
