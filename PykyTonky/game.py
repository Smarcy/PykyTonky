"""Contains the main game loop"""
from PykyTonky.misc import colors, clearScreen
from PykyTonky.model.actors import Player
from PykyTonky.factories.item_factory import weapons
import PykyTonky.factories.room_factory as rFac


def change_location(player, choice):
    player.currentRoom = player.currentRoom.doors[choice-1].targetRoom


def start_game(name):
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
        clearScreen()
        print(
            f"Current Location: ",
            colors.RED,
            f"{player.currentRoom}\n",
            colors.RESET)

        i = 0
        for door in player.currentRoom.doors:
            i += 1
            print(f"[{i}]", door.targetRoom)

        i += 1
        print(f"[{i}] Print Player Info")

        # Check if Input is in range && actually a number
        try:
            option = int(input("> "))
            if option == i:
                print(player.print_player_info())
                input()
                continue
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

        print("Location: {}".format(player.currentRoom))
