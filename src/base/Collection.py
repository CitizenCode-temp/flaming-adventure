import os
import binascii as ba

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
    
