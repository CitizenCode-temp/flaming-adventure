import FACollections
import FAInputController
import FAAppStepper
import FAViews
import FAEventScheduler
import curses

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    # sets up the game resources -- maps, npcs, etc..
    self.appColl = FACollections.AppCollection()

  def run(self,screen):
    curses.echo()
    screen.scrollok(True)

    # Setup game resources
    self.appColl.init_resources()

    # These guys need screen
    self.appView = FAViews.AppView(self, screen)
    self.eventScheduler = FAEventScheduler.EventScheduler()
    self.inputController = FAInputController.InputController(self.appView)
    self.appStepper = FAAppStepper.AppStepper()
    
    self.appView.refresh()
    self.appStepper.run()


app = App()
