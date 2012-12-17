import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import FAParsers.kadvParser as kp
import curses
import Events

class InputController:
  def __init__(self, screen, appCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.parser = kp.kadvParser(self).parser
    self.cmdHistory = []

  def notify(self, event):
    if isinstance(event, Events.InputEvent):
      self.parseCmd( event.getInputStr() )

  def parseCmd(self, cmd):
    self.parser.parse(cmd)

  def log( self, text ):
    logEvent = Events.LogMsgEvent( text )
    self.appCollection.notify( logEvent )

  def quit( self ):
    self.appCollection.notify( Events.QuitEvent() )

"""
  def parseCmd(self, cmd):
     cmdArr = cmd.split(" ")
     self.cmdHistory.append(cmd)
     if len( cmdArr  ) > 0:
       if cmdArr[0] == "log":
         mvEvent = Events.LogMsgEvent(" ".join(cmdArr[1:]))
         self.appCollection.notify( mvEvent )

       if cmdArr[0] == "quit":
       if cmdArr[0] == "go":
         mvEvent = Events.MoveEvent(int(cmdArr[1]), int(cmdArr[2]))
         self.appCollection.notify( mvEvent )
"""
