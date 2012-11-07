"""
  Events Module
  
    A key goal of this code is to demonstrate the power of object-oriented design.
  A part of this is the use of the Mediator/Observer Pattern in which objects
  communicate in one directional, or one to many object Events.
    Care should be taken not to overburder iterating through collections with
  messages. Perhaps a direct function call is in order?
"""

class Event:
  def __init__(self):
    self.name = "Event"

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
