import adv
import events

class AppStepper:
    def __init__(self):
        self.keep_going = True
        self.appCollection = adv.app.appColl
        self.appCollection.add(self)

    def is_stepping(self):
        return self.keep_going

    def run(self):
        while (self.keep_going):
          event = events.StepEvent()
          self.appCollection.notify(event)

    def notify(self, event):
        if isinstance(event, events.PlayerDeathEvent):
            # The player has died.
            self.notify(events.QuitEvent())

        if isinstance(event, events.QuitEvent):
            self.keep_going = False
            adv.app.game_quit() 
        return True

    def restart(self):
        self.keep_going = True
        self.run()
