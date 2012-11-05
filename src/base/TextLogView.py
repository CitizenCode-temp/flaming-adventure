class TextLogView:
  def __init__(self, collection):
    self.coll = collection
    self.coll.add(self)

  def notify(self, event):
    print("\n" + event.getName())

  def log(self, txt):
    print(txt)
