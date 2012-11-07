import curses
import Events

class InputController:
  def __init__(self, screen, appCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, Events.InputEvent):
      self.parseCmd( event.getInputStr() )

  def parseCmd(self, cmd):
     self.cmdHistory.append(cmd)
     if cmd == "quit":
       self.appCollection.notify( Events.QuitEvent() )

