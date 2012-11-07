import curses
import Events

class InputController:
  def __init__(self, screen, appCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, Events.StepEvent):
      # Data comes in as bytes
      string = self.screen.getstr(0,0,80).decode()
      self.cmdHistory.append(string)
      if string == "quit":
        self.appCollection.notify( Events.QuitEvent() )
    return True
