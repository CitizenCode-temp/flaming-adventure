import curses
import Events

class InputController:
  def __init__(self, screen, appCollection):
    self.screen = screen
    self.appCollection = appCollection
    self.appCollection.add(self)

  def notify(self, event):
    if isinstance(event, Events.StepEvent):
      ch_input = self.screen.getch()
      if ch_input == 'q':
        self.appCollection.notify( Events.QuitEvent() )
    return True
