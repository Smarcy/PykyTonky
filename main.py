"""Main Game File"""

import factories.actor_factory as aFac
import sys

player = aFac.getPlayer()


def newGame():
    print("New Game chosen")


def loadGame():
    print("Load Game chosen")


def changeSettings():
    print("Change settings chosen")


print("\nMain Menu\n\n"
      "[1] New Game\n"
      "[2] Load Game\n"
      "[3] Settings\n"
      "[4] Quit\n")


def chosenOption(argument):
    switcher = {
            '1': lambda: newGame(),
            '2': lambda: loadGame(),
            '3': lambda: changeSettings(),
            '4': lambda: sys.exit()
        }
    return switcher.get(argument, lambda: "fail")()


chosenOption(input("> "))
