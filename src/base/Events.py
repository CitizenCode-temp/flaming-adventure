class Event:
  def __init__(self):
    self.name = "Default Event Name"

  def getName(self):
    return self.name

class StepEvent(Event):
  """
  A StepEvent is fired by the AppStepper for each turn (step). 
  """
  def __init__(self):
    self.name = "TickEvent"

class QuitEvent(Event):
  """
  A QuitEvent is fired by the InputController. This stops listening
  AppSteppers.
  """
  def __init__(self):
    self.name = "QuitEvent"
