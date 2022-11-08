#游戏主要入口

from source import tools
from source import tools, setup
from source.states import main_menu, load_screen, level

def main():

    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level()
    }
    game = tools.Game(state_dict, 'main_menu')

    #state = main_menu.MainMenu()
    #state = load_screen.LoadScreen()
    #state = level.Level()
    game.run()

if __name__ == '__main__':
    main()