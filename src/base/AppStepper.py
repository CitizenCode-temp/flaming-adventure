import Event

class AppStepper:
  def __init__(self,appCollection):
    self.keep_going = True
    self.appCollection = appCollection

  def run(self):
    while (self.keep_going):
      event = Event.Event()
      self.appCollection.notify(event)

  def notify(self, event):
    return True
      
