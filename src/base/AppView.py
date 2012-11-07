import curses
import Collection
import Events
"""
  AppView

    AppView is the main view object for the application. It holds
  references to the sub-view objects for messaging and rendering
  purposes.

"""

class AppView:
  def __init__(self, model, screen, appCollection):
    self.model = model
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)

    self.viewCollection = Collection.Collection()
    self.cmdLine = self.createCmdLineWindow(3)
    self.viewCollection.add(self.cmdLine)

  def refresh(self):
    self.cmdLine.scroll(-1)
    self.screen.refresh()

  def notify(self, event):
    if isinstance(event, Events.StepEvent):
      self.viewCollection.notify(event)

  def getCmdLineView(self):
    return self.cmdLine
