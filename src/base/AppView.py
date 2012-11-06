import curses

class AppView:
  def __init__(self, model, screen, appCollection):
    self.model = model
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)

  def render(self):
    self.screen.addch(0,0,"X")
    self.screen.refresh()

  def notify(self, event):
    self.render()
