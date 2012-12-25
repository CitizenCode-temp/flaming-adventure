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
    self.name = "StepEvent"

class QuitEvent(Event):
  """
  This stops listening AppSteppers.
  """
  def __init__(self):
    self.name = "QuitEvent"

class MoveEvent(Event):
  """
  Fired when a keyboard movement is detected.
  """
  def __init__(self,Dx=0,Dy=0):
    self.name = "MoveEvent"
    self.Dx = Dx
    self.Dy = Dy

  def getDx(self):
    return self.Dx

  def getDy(self):
    return self.Dy
 
class LogMsgEvent(Event):
  def __init__(self, msg):
    self.name = "LogMsgEvent"
    self.msg = msg

  def getMsg(self):
    return self.msg

class DialogEvent(Event):
  def __init__(self, obj):
    self.name = "DialogEvent"
    self.description = obj.getDescription()

  def getDescription(self):
    return self.description
