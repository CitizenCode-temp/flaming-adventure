"""
  Collection

    A collection provides an abstraction for working with sets of other objects.
  One important role they play is forwarding Events to their members via the
  notify function.
"""

class Collection:
  def __init__(self):
    self.members = []

  def __len__(self):
    return len( self.members )

  def add(self, obj):
    if (self.members.count(obj) == 0):
      self.members.append(obj) 

  def remove(self, obj):
    self.members.remove(obj)

  def forEach(func):
    for m in self.members:
      func(m)

  def notify(self, event):
    for m in self.members:
      m.notify(event)

class AppCollection(Collection):
  def __init__(self):
    self.members = []
    self.mapCollection = Collection() 
  
  def notifyMaps(self, event):
    self.mapCollection.notify(event)
