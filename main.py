"""Main Game File"""

import factories.actor_factory as aFac
import factories.item_factory as iFac
import game
import sys

player = None


def new_game():
    name = input("Choose a name: ")
    player = aFac.createPlayer(name, 100, 1, 0, iFac.weapons["shortsword"])

    game.start_game(player)


def load_game():
    print("Load Game chosen")


def change_settings():
    print("Change settings chosen")


def chosen_option(argument):
    switcher = {
            '1': lambda: new_game(),
            '2': lambda: load_game(),
            '3': lambda: change_settings(),
            '4': lambda: quit()
        }
    return switcher.get(argument, lambda: "fail")()


print("\nMain Menu\n\n"
      "[1] New Game\n"
      "[2] Load Game\n"
      "[3] Settings\n"
      "[4] Quit\n")

chosen_option(input("> "))
