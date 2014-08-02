class Model(object):
  def __init__(self, _id, *args, **kwargs):
    super(Model, self).__init__(_id, *args, **kwargs)
    self._id = _id 

  def notify( self, event ):
    return True 

  def getId(self):
    return self._id
