import Collection
import InputController
import AppStepper
import Model
import AppView
import EventScheduler
import curses

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    self.appColl = Collection.Collection()
    self.appColl.add(self)
    #self.modelCollection = Collection.Collection()
    #self.viewCollection = Collection.Collection()

    self.timedColl = Collection.Collection()
    
  def run(self,screen):
    curses.echo()
    screen.scrollok(True)
    self.eventScheduler = EventScheduler.EventScheduler(self.appColl)
    self.appView = AppView.AppView(self, screen, self.appColl)
    self.inputController = InputController.InputController(self.appView.getCmdLineView(), self.appColl)
    self.appStepper = AppStepper.AppStepper(self.appColl)

    self.appStepper.run()

  def notify(self, event):
    return True

def main():
  app = App()
  curses.wrapper( app.run )

if __name__ == "__main__":
  main()
  
