import adv
import events

class AppStepper:
  def __init__(self):
    self.keep_going = True
    self.appCollection = adv.app.appColl
    self.appCollection.add(self)

  def run(self):
    while (self.keep_going):
      event = events.StepEvent()
      self.appCollection.notify(event)

  def notify(self, event):
    if isinstance(event, events.QuitEvent):
      self.keep_going = False
    return True
