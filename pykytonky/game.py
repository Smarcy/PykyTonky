"""Contains the main game loop"""
import sys

from pykytonky.misc import Colors, clear_screen
from pykytonky.model.actors import Player
from pykytonky.factories.item_factory import weapons
import pykytonky.factories.room_factory as rFac


def change_location(player, choice):
    """Change the Players room accordingly"""
    player.current_room = player.current_room.doors[choice-1].target_room


def start_game(name):
    """Main Game Loop"""
    run = True

    player = None

    # Check if Player is already set so the currentRoom stays the same after
    # printPlayer Info
    try:
        player = Player(
            name, 100, 1, 0, weapons["shortsword"],
            rFac.rooms["Living Room"])
    except NameError:
        pass

    while run:
        clear_screen()
        print(
            "Name:             ",
            Colors.BLUE,
            f"{player.name}",
            Colors.RESET)
        print(
            "Current Location: ",
            Colors.RED,
            f"{player.current_room}\n",
            Colors.RESET)

        i = 0
        for door in player.current_room.doors:
            i += 1
            print(f"[{i}]", door.target_room)

        i += 1
        print(f"[{i}] Print Player Info")
        print(f"[{i+1}] Quit")

        # Check if Input is in range && actually a number
        try:
            option = int(input("> "))
            if option == i:
                print(player.print_player_info())
                input()
                continue
            if option == i+1:
                sys.exit()
            if option > i or option < 1:
                print("No valid Input!")
                input()
                start_game(name)
            else:
                change_location(player, option)
        except ValueError:
            print("Input must be a number!")
            input()
            start_game(name)

        print("Location: {}".format(player.current_room))
