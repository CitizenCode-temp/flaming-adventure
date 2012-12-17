import Collections
import InputController
import AppStepper
import Models
import Events
import Views
import EventScheduler
import curses

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    self.player = Models.Player("player0")
    self.appColl = Collections.AppCollection(self.player)
    self.appColl.add(self)
    
  def run(self,screen):
    curses.echo()
    screen.scrollok(True)
    self.appView = Views.AppView(self, screen, self.appColl)

    self.eventScheduler = EventScheduler.EventScheduler(self.appColl)
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
  
