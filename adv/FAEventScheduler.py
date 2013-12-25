import FAEvents

"""
  EventScheduler

    This keeps an internal array of Events and an associated delay time.
  Every time a StepEvent is caught it calls doTurn() and does turnLength's
  worth of 'times' tasks.

  Assuming turnLength = 1.0
  queue: [0.1, ThisTurnEvent], [1.2, NextTurnEvent], [3.0 LongTimeEvent], ...

  addEvent( event, delayTime ) - Add an event to the queue
  getEvent() - Pop the 0th tuple off the queue and return the event
  doTurn() - Do turnLength's worth of events (notify the appCollection)
             Should probably be only internally used.
"""
class EventScheduler:
  def __init__(self, appCollection):
    self.queue = []
    self.appCollection = appCollection
    self.appCollection.add(self)
    self.turnLength = 1.00

  def __len__(self):
    return len( self.queue )

  def notify(self, event):
    if isinstance(event, FAEvents.StepEvent):
      self.doTurn()

  def addEvent(self, event, delay=0.00):
    delayedEvent = [delay, event]
    self.queue.insert( self.getQueueIndex(delay), delayedEvent )

  def getEvent(self):
    if (len(self.queue) < 1):
      return None
    return self.queue.pop(0)[1]

  def doTurn(self):
    while( self.getFirstDelay() is not None and self.getFirstDelay() < self.turnLength ):
      self.appCollection.notify( self.getEvent() )
    self.adjustDelays(-self.turnLength)

  def getFirstDelay(self):
    if len( self.queue ) < 1:
      return None
    else:
      return self.queue[0][0]

  def adjustDelays(self, delay):
    for t in self.queue:
      t[0] += delay

  def getDelayedEventTuple(self):
    if (len(self.queue) < 1):
      return [0.00, None]
    return self.queue.pop(0)

  def getQueueIndex(self, delay ):
    if len( self.queue ) == 0:
      return 0

    for index_f in range( len( self.queue ) ):
      if (self.queue[ index_f ][0] > delay):
        return index_f

    return len( self.queue )
