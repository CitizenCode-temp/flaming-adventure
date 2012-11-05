import Event
import Collection
import Model
import TextLogView

class App:
  def __init__(self):
    # appColl -- used for application level event notification
    self.appColl = Collection.Collection()
    self.appColl.add(self)
    
    self.appView = TextLogView.TextLogView(self.appColl)
    
  def run(self):
    self.appColl.notify( Event.Event() )

  def notify(self, event):
    return True

def main():
  app = App()
  app.run()

if __name__ == "__main__":
  main()
  


