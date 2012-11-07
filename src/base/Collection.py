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

"""
class AppCollection:
  def __init__(self):
    self.add(self.modelCollection)
    self.add(self.viewCollection)
  
  def notifyModels(self, event):
    self.modelCollection.notify(event)

  def notifyViews(self, event):
    self.viewCollection.notify(event)
"""
