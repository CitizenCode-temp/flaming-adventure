import FAEvents

class AppStepper:
  def __init__(self,appCollection):
    self.keep_going = True
    self.appCollection = appCollection
    self.appCollection.add(self)

  def run(self):
    while (self.keep_going):
      event = FAEvents.StepEvent()
      self.appCollection.notify(event)

  def notify(self, event):
    if isinstance(event, FAEvents.QuitEvent):
      self.keep_going = False
    return True
