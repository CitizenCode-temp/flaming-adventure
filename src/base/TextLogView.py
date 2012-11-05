class TextLogView:
  def __init__(self, evManager):
    self.evManager = evManager
    self.evManager.registerListener(self)

  def notify(self, event):
    print(event.getName())
