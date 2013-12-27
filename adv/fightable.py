import events

class Fightable(object):
    def __init__(self, *args, **kwargs):
        super(Fightable, self).__init__()
        self.fightable = True

    def do_combat(self, char):
      if hasattr(char, 'fightable'):
        self.appCollection.notify(
          events.LogMsgEvent(
            "{0} fightable resolving against {1}".format(
                self.name,
                char.getName()
            )
          )
        )
