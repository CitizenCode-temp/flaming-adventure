import adv
import events

class Parser:
  def __init__(self, inputController):
    self.appCollection = adv.app.appColl
    self.inputController = inputController
    self.lookDict = self.initLookDictionary()

  def parseChar(self, char):
    if char == 105: # i -- insert mode
      self.inputController.getInsertModeCmd()
    if char == 104: # h -- left
      mvEvent = events.MoveEvent(-1, 0)
      self.appCollection.notify( mvEvent )
    if char == 106: # j -- down
      mvEvent = events.MoveEvent(0, 1)
      self.appCollection.notify( mvEvent )
    if char == 107: # k -- up
      mvEvent = events.MoveEvent(0, -1)
      self.appCollection.notify( mvEvent )
    if char == 108: # l -- right 
      mvEvent = events.MoveEvent(1, 0)
      self.appCollection.notify( mvEvent )

  def parse(self, cmd):
    cmdArr = cmd.split(" ")
    if len( cmdArr  ) > 0:
      if cmdArr[0] == "log":
        logEvent = events.LogMsgEvent(" ".join(cmdArr[1:]))
        self.appCollection.notify( logEvent )

      if cmdArr[0] == "quit":
        self.appCollection.notify( events.QuitEvent() )

      if cmdArr[0] == "go":
        mvEvent = events.MoveEvent(int(cmdArr[1]), int(cmdArr[2]))
        self.appCollection.notify( mvEvent )

      if cmdArr[0] == "look":
        if len( cmdArr ) != 2:
          return False

        self.parseLook( cmdArr[1] )
      
      return True

  def parseLook(self, lookKey):
    lookObj = self.lookDict[ lookKey ]  
    if lookObj:
      dialogEvent = events.DialogEvent( lookObj )
      self.appCollection.notifyAppView( dialogEvent )

  def initLookDictionary(self):
      return { 
        'me': self.appCollection.getPlayer()
         }
