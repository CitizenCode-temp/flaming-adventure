import random

class Fightable(object):
    def __init__(self, *args, **kwargs):
        super(Fightable, self).__init__()
        self.fightable = True

    def do_combat(self, char):
      def resolve_speed(c1, c2):
          s1 = c1.get_speed()
          s2 = c2.get_speed()
          if s1 > s2:
            return c1, c2
          elif s1 < s2:
            return c2, c1
          else:
            l = [c1, c2]
            r = random.choice(l)
            l.remove(r)
            return r, l[0]
            

      if hasattr(char, 'fightable'):
        first, second = resolve_speed(self, char)        
        first.attack(second)
        if second.is_alive():
          second.attack(first)

    def attack(self, char):
        damage = self.strength - char.get_defense()
        char.set_health(char.get_health() - damage)
