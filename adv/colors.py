import curses

def get_colors(key):
    bg_color = 234
    # Player
    curses.init_pair(1, curses.COLOR_MAGENTA, bg_color)
    # Monster
    curses.init_pair(2, curses.COLOR_RED, bg_color)
    # Wall
    curses.init_pair(3, curses.COLOR_WHITE, bg_color)
    # Floor 
    curses.init_pair(4, 242, bg_color)

    colors = {
        'default': curses.color_pair(0),
        'player': curses.color_pair(1),
        'monster': curses.color_pair(2),
        'wall':  curses.color_pair(3),
        'floor': curses.color_pair(4),
    }

    return colors.get(key)
