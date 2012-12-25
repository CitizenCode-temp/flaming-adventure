import FAEvents

class Parser:
  def __init__(self, inputController, appCollection):
    self.appCollection = appCollection
    self.inputController = inputController

  def parseChar(self, char):
    if char == 105: # i -- insert mode
      self.inputController.getInsertModeCmd()

  def parse(self, cmd):
     cmdArr = cmd.split(" ")
     if len( cmdArr  ) > 0:
       if cmdArr[0] == "log":
         logEvent = FAEvents.LogMsgEvent(" ".join(cmdArr[1:]))
         self.appCollection.notify( logEvent )

       if cmdArr[0] == "quit":
         self.appCollection.notify( FAEvents.QuitEvent() )

       if cmdArr[0] == "go":
         mvEvent = FAEvents.MoveEvent(int(cmdArr[1]), int(cmdArr[2]))
         self.appCollection.notify( mvEvent )
