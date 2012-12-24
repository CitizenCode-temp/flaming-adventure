import curses
import FACollections
import FAEvents
"""
  View
"""

class View:
  def __init__(self, model, screen, collection):
    self.model = model
    self.screen = screen
    self.collection = collection
    self.collection.add(self)

  def refresh(self):
    self.screen.refresh()

  def notify(self, event):
    if isinstance(event, FAEvents.StepEvent):
      self.refresh()

"""
  AppView

    AppView is the main view object for the application. It holds
  references to the sub-view objects for messaging and rendering
  purposes.

"""
class AppView(View):
  def __init__(self, model, screen, appCollection):
    self.model = model
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)

    windowHeight = self.screen.getmaxyx()[0]
    windowWidth = self.screen.getmaxyx()[1]
    cmdLineHeight = 3
    statusHeight = 3
    mapHeight = windowHeight - cmdLineHeight - statusHeight
    
    self.viewCollection = FACollections.Collection()
    self.mapView = MapView(mapHeight, windowWidth, self.appCollection, self.viewCollection)
    self.statusView = StatusView(statusHeight, (windowHeight - cmdLineHeight), windowWidth, self.appCollection, self.viewCollection)
    self.cmdLineView = CmdLineView(cmdLineHeight, windowHeight, windowWidth, self.appCollection, self.viewCollection)

  def refresh(self):
    self.mapView.refresh()
    self.statusView.refresh()
    self.cmdLineView.refresh()

  def notify(self, event):
    if isinstance(event, FAEvents.StepEvent):
      self.viewCollection.notify(event)
    if isinstance(event, FAEvents.LogMsgEvent):
      self.statusView.logMsg( event.getMsg() )

  def getCmdLineView(self):
    return self.cmdLineView

class CursesView(View):
  def __init__(self, height, windowHeight, windowWidth, appCollection, viewCollection):
    self.screen = curses.newwin(height, windowWidth, windowHeight-height, 0) 
    self.screen.scrollok(True)
    self.appCollection = appCollection
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

  def refresh(self):
    self.screen.refresh()

  def notify(self,event):
    self.refresh()

class CmdLineView(CursesView):
  def refresh(self):
    self.screen.scroll(-1)

  def notify(self, event):
    if isinstance(event, FAEvents.StepEvent):
      string = self.screen.getstr(0,0,80).decode()
      ev = FAEvents.InputEvent(string)
      self.refresh()
      self.appCollection.notify(ev)

class StatusView(CursesView):
  def __init__(self, height, windowHeight, windowWidth, appCollection, viewCollection):
    self.screen = curses.newwin(height, windowWidth, windowHeight-height, 0) 
    self.screen.scrollok(True)
    self.appCollection = appCollection
    self.viewCollection = viewCollection
    self.viewCollection.add(self)
    self.msgLog = []

  def refresh(self):
    self.screen.clear() 

    name = self.appCollection.getPlayer().getName()
    hp = str( self.appCollection.getPlayer().getHealth() )
    maxHp = str( self.appCollection.getPlayer().getMaxHealth() )
    level = str( self.appCollection.getPlayer().getLevel() )

    self.screen.addstr(0,0, name + " Lvl " + level + " | A5 D3 S1 | HP " + hp + "/" + maxHp)

    if (len( self.msgLog ) > 0):
      self.screen.addstr(1,0,self.msgLog[0])
    else:
      self.screen.addstr(1,0,"")

    if (len( self.msgLog ) > 1):
      self.screen.addstr(2,0,self.msgLog[1])
    else:
      self.screen.addstr(2,0,"")

    self.screen.refresh()

  def logMsg(self, msg):
    self.msgLog.insert(0,msg)

class MapView(CursesView):
  def __init__(self, height, windowWidth, appCollection, viewCollection):
    self.screen = curses.newwin(height, windowWidth, 0, 0) 
    self.screen.scrollok(True)
    self.appCollection = appCollection
    self.mapCollection = self.appCollection.getMapCollection()
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

    self.playerView = PlayerView(self.screen, appCollection, viewCollection)

  def refresh(self):
    self.refreshMap()
    self.playerView.refresh()
    self.screen.refresh()

  def refreshMap(self):
    currMap = self.mapCollection.getCurrentMap()
    mapArr = currMap.getMapArray()
    for x in range(currMap.getWidth()):
      for y in range(currMap.getHeight()):
        self.screen.addstr(y, x, mapArr[x][y].getStrRep())

class PlayerView(View):
  def __init__(self, screen, appCollection, viewCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.player = appCollection.getPlayer()
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

  def refresh(self):
    x, y = self.player.getXY()
    self.screen.addstr(y,x,"@")

  def notify(self,event):
    return True
