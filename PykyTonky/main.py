"""Main Game File"""

import PykyTonky.factories.room_factory as rFac
import PykyTonky.factories.door_factory as dFac
from PykyTonky.misc import clearScreen
import PykyTonky.game as game


def new_game():
    rFac.createRooms()
    dFac.createDoors()
    name = input("Choose a name: ")

    game.start_game(name)


def load_game():
    print("Load Game chosen")
    input()
    show_intro()


def change_settings():
    print("Change settings chosen")
    input()
    show_intro()


def chosen_option(argument):
    switcher = {
        '1': lambda: new_game(),
        '2': lambda: load_game(),
        '3': lambda: change_settings(),
        '4': lambda: quit()
    }
    return switcher.get(argument, lambda: "fail")()


def show_intro():

    clearScreen()
    print("Main Menu\n\n"
          "[1] New Game\n"
          "[2] Load Game\n"
          "[3] Settings\n"
          "[4] Quit\n")

    chosen_option(input("> "))


if __name__ == "__main__":
    show_intro()
