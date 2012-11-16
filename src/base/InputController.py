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
     cmdArr = cmd.split(" ")
     self.cmdHistory.append(cmd)
     if len( cmdArr  ) > 0:
       if cmdArr[0] == "test":
         mvEvent = Events.MoveEvent(1, 1)
         self.appCollection.notify( mvEvent )

       if cmdArr[0] == "quit":
         self.appCollection.notify( Events.QuitEvent() )
       if cmdArr[0] == "go":
         mvEvent = Events.MoveEvent(int(cmdArr[1]), int(cmdArr[2]))
         self.appCollection.notify( mvEvent )
