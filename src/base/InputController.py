import curses

class InputController:
  def __init__(self, screen, appCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)

  def notify(self, event):
    input = self.screen.getch()
