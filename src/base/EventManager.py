class EventManager:
  def __init__(self):
    self.listeners = []

  def registerListener( self, listener ):
    self.listeners.append( listener )

  def unregisterListener( self, listener ):
    if listener in self.listeners:
      self.listeners.remove( listener ) 

  def notify( self, event ):
    for listener in self.listeners:
      listener.notify( event )
