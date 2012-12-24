import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import Events

class faParser:
  def __init__(self, inputController, appCollection):
    self.appCollection = appCollection
    self.inputController = inputController

  def parse(self, cmd):
     cmdArr = cmd.split(" ")
     if len( cmdArr  ) > 0:
       if cmdArr[0] == "log":
         mvEvent = Events.LogMsgEvent(" ".join(cmdArr[1:]))
         self.appCollection.notify( mvEvent )

       if cmdArr[0] == "quit":
         self.appCollection.notify( Events.QuitEvent() )

       if cmdArr[0] == "go":
         mvEvent = Events.MoveEvent(int(cmdArr[1]), int(cmdArr[2]))
         self.appCollection.notify( mvEvent )
