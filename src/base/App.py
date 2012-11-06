import Event
import Collection
import InputController
import AppStepper
import Model
import AppView
import curses

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    self.appColl = Collection.Collection()
    self.appColl.add(self)
    
  def run(self,screen):
    self.inputController = InputController.InputController(screen, self.appColl)
    self.appView = AppView.AppView(self, screen, self.appColl)
    self.appStepper = AppStepper.AppStepper(self.appColl)

    self.appStepper.run()

  def notify(self, event):
    return True

def main():
  app = App()
  curses.wrapper( app.run )

if __name__ == "__main__":
  main()
  
