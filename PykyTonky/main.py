"""Main Game File"""

import factories.room_factory as rFac
import factories.door_factory as dFac
from misc import clearScreen
import game as game


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
        1: lambda: new_game(),
        2: lambda: load_game(),
        3: lambda: change_settings(),
        4: lambda: quit()
    }
    return switcher.get(argument, lambda: "fail")()


def show_intro():

    clearScreen()
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
