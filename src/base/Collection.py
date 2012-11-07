import os
import Events
import Collection

class Collection:
  def __init__(self):
    self.members = []

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

  def getLength(self):
    return len( self.members )
    
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
