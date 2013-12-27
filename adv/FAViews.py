import adv
import characters
import colors
import curses
import FACollections
import events
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
    self.screen.noutrefresh()
    return True

  def notify(self, event):
    if isinstance(event, events.StepEvent):
      self.refresh()
    return True

"""
  AppView

    AppView is the main view object for the application. It holds
  references to the sub-view objects for messaging and rendering
  purposes.

"""
class AppView(View):
  def __init__(self, model, screen):
    self.model = model
    self.screen = screen
    self.appCollection = adv.app.appColl
    self.appCollection.setAppView(self)
    if not self.appCollection.getAppView():
      raise Exception("No appView in appCollection?")

    windowHeight = self.screen.getmaxyx()[0]
    windowWidth = self.screen.getmaxyx()[1]
    cmdLineHeight = 3
    statusHeight = 4
    mapHeight = windowHeight - cmdLineHeight - statusHeight
    descVisHeight = 10 
    descVisWidth = 40
    
    self.viewCollection = FACollections.Collection()
    self.mapView = MapView(mapHeight, windowWidth, self.viewCollection)
    self.statusView = StatusView(statusHeight, (windowHeight - cmdLineHeight), windowWidth, self.viewCollection)
    self.cmdLineView = CmdLineView(cmdLineHeight, windowHeight, windowWidth, self.viewCollection)
    self.dialogView = DialogView( descVisHeight, descVisWidth, 1, 10, self.viewCollection)

  def notify(self, event):
    self.viewCollection.notify(event)
    return True

  def refresh(self):
    self.mapView.refresh()
    self.statusView.refresh()
    # Don't refresh cmdLineView
    #self.cmdLineView.refresh()
    self.screen.refresh()
    return True
    
  def getCmdLineView(self):
    return self.cmdLineView

  def getStatusView(self):
    return self.statusView

class DialogView(View):
  def __init__(self, height, width, yOffset, xOffset, viewCollection):
    self.height = height
    self.width = width
    self.yOffset = yOffset
    self.xOffset = xOffset
    self.outerScreen = curses.newwin(height + 3, width + 2, self.yOffset - 1, self.xOffset -1)
    self.screen = curses.newpad(100, width) 
    self.screen.scrollok(True)
    self.appCollection = adv.app.appColl
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

  def notify(self, event):
    if isinstance(event, events.DialogEvent):
      self.refresh( event.getDescription() )

  def refresh(self, txt):
    # Compute row and scrolling information
    currRow = 0
    nTxtRows = (len( txt ) // self.width) + 3 # + 1 due to array indexing and + 2 for the documentation and newline
    maxRow = 0
    if nTxtRows > self.height:
      maxRow = nTxtRows - self.height

    curses.noecho()
    self.screen.clear()
    self.screen.addstr(0, 0, "j/k -- scroll down/up | y/n -- yes/no, q -- quit") # Documentation line
    self.screen.addstr(2, 0, txt)

   
    # Enter loop with simple interactivity
    while True:
      self.outerScreen.box()
      self.outerScreen.noutrefresh()
      self.screen.refresh(currRow, 0, self.yOffset, self.xOffset, self.yOffset + self.height, self.xOffset + self.width)
      c = self.screen.getch()
      if c == 106 and currRow < maxRow: # j scroll down
        currRow += 1
      if c == 107 and currRow > 0: # k scroll up
        currRow -= 1
      if c == 113: # q quit dialog
        break

    self.outerScreen.clear()
    self.outerScreen.noutrefresh()
    self.screen.clear()
    self.screen.refresh(currRow, 0, 1, self.xOffset, 11, self.xOffset + self.width)
    curses.echo()

class CursesView(View):
  def __init__(self, height, windowHeight, windowWidth, viewCollection):
    self.screen = curses.newwin(height, windowWidth, windowHeight-height, 0) 
    self.screen.scrollok(True)
    self.appCollection = adv.app.appColl
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

  def refresh(self):
    self.screen.noutrefresh()
    return True

  def notify(self,event):
    if isinstance(event, events.StepEvent):
      self.refresh()
    return True

class CmdLineView(CursesView):
  def getCh(self):
    curses.noecho()
    char = self.screen.getch(0,0) # Get the command, off the screen!
    curses.echo()
    return char

  def getStrCmd(self):
    string = self.screen.getstr(0,0,80).decode()
    self.screen.scroll(-1)
    return string

class StatusView(CursesView):
  def __init__(self, height, windowHeight, windowWidth, viewCollection):
    self.screen = curses.newwin(height, windowWidth, windowHeight-height, 0) 
    self.screen.scrollok(True)
    self.appCollection = adv.app.appColl
    self.viewCollection = viewCollection
    self.viewCollection.add(self)
    self.msgLog = ["You search futily for light in the dark cave"]
    self.lastCmd = ""
    self.statusFlag = "Cmd Mode"

  def setStatusFlag( self, msg ):
    self.statusFlag = msg
    self.refresh()

  def setLastCmd( self, lastCmd ):
    self.lastCmd = lastCmd
    self.refresh()

  def refresh(self):
    self.screen.clear() 

    name = self.appCollection.getPlayer().get_name()
    hp = str( self.appCollection.getPlayer().get_health() )
    maxHp = str( self.appCollection.getPlayer().get_max_health() )
    level = str( self.appCollection.getPlayer().get_level() )

    self.screen.addstr(0,0, name + " Lvl " + level + " | A5 D3 S1 | HP " + hp + "/" + maxHp + " | " + self.statusFlag + " | " + self.lastCmd)

    if (len( self.msgLog ) > 0):
      self.screen.addstr(1,0,self.msgLog[0])
    else:
      self.screen.addstr(1,0,"")

    if (len( self.msgLog ) > 1):
      self.screen.addstr(2,0,self.msgLog[1])
    else:
      self.screen.addstr(2,0,"")

    self.screen.noutrefresh()

  def logMsg(self, msg):
    self.msgLog.insert(0,msg)

  def notify(self, event):
    if isinstance(event, events.LogMsgEvent):
      self.logMsg( event.getMsg() )
    if isinstance(event, events.StepEvent):
      self.refresh()
    return True

class NPCView(View):
  def __init__(self, screen, npc):
    self.npc = npc
    self.screen = screen
    if isinstance(npc, characters.Monster):
        self.color = colors.get_colors('monster')
    else:
        self.color = colors.get_colors('default')

  def refresh(self):
    x, y = self.npc.getXY()
    self.screen.addstr(y, x, self.npc.get_char(), self.color)


class MapView(CursesView):
  """
    A notifieable view which contains references to the map collection as
    well as player and npc views.
  """
  def __init__(self, height, windowWidth, viewCollection):
    self.outerScreen = curses.newwin(height, windowWidth, 0, 0) 
    self.outerScreen.border(0)
    self.screen = curses.newwin(height-2, windowWidth-2, 1, 1) 
    self.screen.scrollok(True)
    self.appCollection = adv.app.appColl
    self.mapCollection = self.appCollection.getMapCollection()
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

    self.playerView = PlayerView(self.screen, self.appCollection.getPlayer())

    self.npc_views = []
    npcs = self.mapCollection.getCurrentMap().get_npcs()
    for n in npcs:
        v = NPCView(self.screen, n)
        self.npc_views.append(v)

  def refresh(self):
    self.screen.clear()
    self.outerScreen.box()
    self.outerScreen.noutrefresh()
    self.refreshMap()
    for v in self.npc_views:
        v.refresh()
    self.playerView.refresh()
    self.screen.noutrefresh()
  
  def get_sector_colors(self, str_rep):
      sector_colors = {
          '.': colors.get_colors('floor'),
          '#': colors.get_colors('wall')
      }
      return sector_colors.get(str_rep, colors.get_colors('default'))

  def refreshMap(self):
    # TODO make sure the screen is big enough
    currMap = self.mapCollection.getCurrentMap()
    mapArr = currMap.getMapSectorArray()
    for x in range(currMap.getWidth()):
      for y in range(currMap.getHeight()):
            s = mapArr[x][y].getStrRep()
            c = self.get_sector_colors(s)
            self.screen.addstr(y, x, s, c)

class PlayerView(View):
  def __init__(self, screen, player):
    self.screen = screen
    self.player = player
    self.color = colors.get_colors('player')

  def refresh(self):
    x, y = self.player.getXY()
    self.screen.addstr(y, x, self.player.get_char(), self.color)
