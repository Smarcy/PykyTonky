"""Main Game File"""

import pykytonky.factories.room_factory as rFac
import pykytonky.factories.door_factory as dFac
from pykytonky.misc import clear_screen
import pykytonky.game as game


def new_game():
    """Initiates a new game by choosing a name"""
    rFac.create_rooms()
    dFac.create_doors()
    clear_screen()
    name = input("Choose a name: ")

    game.start_game(name)


def load_game():
    """TODO: Load a saved game"""
    print("Load Game chosen")
    input()
    show_intro()


def change_settings():
    """TODO: Change several Settings"""
    print("Change settings chosen")
    input()
    show_intro()


def chosen_option(argument):
    """Evaluate which option was chosen"""
    switcher = {
        1: new_game,
        2: load_game,
        3: change_settings,
        4: quit
    }
    return switcher.get(argument, lambda: "fail")()


def show_intro():
    """Display intro options and take user input"""
    clear_screen()
    print("Main Menu\n\n"
          "[1] New Game\n"
          "[2] Load Game\n"
          "[3] Settings\n"
          "[4] Quit\n")

    # Check if input is in correct range && actually a number
    try:
        option = int(input("> "))
        if option > 4 or option < 1:
            print("No valid input!")
            input()
            show_intro()
        else:
            chosen_option(option)
    except ValueError:
        print("Input must be a number!")
        input()
        show_intro()


if __name__ == "__main__":
    show_intro()
