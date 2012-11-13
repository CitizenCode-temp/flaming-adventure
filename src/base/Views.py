import curses
import Collections
import Events
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
    if isinstance(event, Events.StepEvent):
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
    
    self.viewCollection = Collections.Collection()
    self.mapView = MapView(mapHeight, windowWidth, self.appCollection, self.viewCollection)
    self.statusView = StatusView(statusHeight, (windowHeight - cmdLineHeight), windowWidth, self.appCollection, self.viewCollection)
    self.cmdLineView = CmdLineView(cmdLineHeight, windowHeight, windowWidth, self.appCollection, self.viewCollection)

  def refresh(self):
    self.mapView.refresh()
    self.statusView.refresh()
    self.cmdLineView.refresh()

  def notify(self, event):
    if isinstance(event, Events.StepEvent):
      self.viewCollection.notify(event)

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
    if isinstance(event, Events.StepEvent):
      string = self.screen.getstr(0,0,80).decode()
      ev = Events.InputEvent(string)
      self.refresh()
      self.appCollection.notify(ev)

class StatusView(CursesView):
  def refresh(self):
    self.screen.addstr(0,0,"Character Info")
    self.screen.addstr(1,0,"Character Info")
    self.screen.addstr(2,0,"Character Info")
    self.screen.refresh()

class MapView(CursesView):
  def __init__(self, height, windowWidth, appCollection, viewCollection):
    self.screen = curses.newwin(height, windowWidth, 0, 0) 
    self.screen.scrollok(True)
    self.appCollection = appCollection
    self.viewCollection = viewCollection
    self.viewCollection.add(self)

  def refresh(self):
    self.screen.addstr(0,0,"I'm a map.")
    self.screen.refresh()
