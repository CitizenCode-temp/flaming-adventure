import Event
import EventManager
import Model
import TextLogView

class App:
  def __init__(self):
    self.appEventMgr = EventManager.EventManager()
    self.appEventMgr.registerListener(self)
    
    self.appView = TextLogView.TextLogView(self.appEventMgr)
    
  def run(self):
    self.appEventMgr.notify( Event.Event() )

  def notify(self, event):
    return True

def main():
  app = App()
  app.run()

if __name__ == "__main__":
  main()
  


