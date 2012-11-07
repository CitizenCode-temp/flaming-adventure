class TaskScheduler:
  def __init__(self, appCollection):
    self.queue = []
    self.appCollection = appCollection
    self.appCollection.add(self)

  def __len__(self):
    return len( self.queue )

  def addTask(self, taskFunc, delay=0.00):
    delayedTask = [delay, taskFunc]
    self.queue.insert( self.getQueueIndex(delay), delayedTask )

  def getTask(self):
    if (len(self.queue) < 1):
      return None
    return self.queue.pop(0)[1]

  def adjustDelays(self, delay):
    for t in self.queue:
      t[0] += delay

  def getDelayedTaskTuple(self):
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
