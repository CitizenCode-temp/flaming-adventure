import FACollections
import FAInputController
import FAAppStepper
import FAViews
import FAEventScheduler
import curses

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    self.appColl = FACollections.AppCollection()
    self.appColl.add(self)

  def run(self,screen):
    curses.echo()
    screen.scrollok(True)

    # These guys need screen
    self.appView = FAViews.AppView(self, screen, self.appColl)
    self.eventScheduler = FAEventScheduler.EventScheduler(self.appColl)
    self.inputController = FAInputController.InputController(self.appView, self.appColl)
    self.appStepper = FAAppStepper.AppStepper(self.appColl)
    
    self.appView.refresh()
    self.appStepper.run()

  def notify(self, event):
    return True

def main():
  app = App()
  curses.wrapper( app.run )

if __name__ == "__main__":
  main()
