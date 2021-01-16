import factories.door_factory as dFac
from misc import clearScreen


def change_location(location):
    switcher = {
            '1': lambda: go_north(),
            '2': lambda: go_east(),
            '3': lambda: go_south(),
            '4': lambda: go_west()
        }

    return switcher.get(location, lambda: "fail")()


def start_game(player):
    run = True

    while run:
        clearScreen()
        print("Welcome to ApplePy!\n")

        i = 1
        for door in player.currentRoom.doors:
            print("[{}]".format(i), door.targetRoom)
            i += 1

        change_location(input("> "))

        input()


def go_north():
    print("went north")


def go_east():
    print("went east")


def go_south():
    print("went south")


def go_west():
    print("went west")
