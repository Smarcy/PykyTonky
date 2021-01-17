"""Contains the main game loop"""

from PykyTonky.misc import colors, clearScreen
from PykyTonky.model.actors import Player
from PykyTonky.factories.item_factory import weapons
import PykyTonky.factories.room_factory as rFac


def change_location(player, choice):
    player.currentRoom = player.currentRoom.doors[choice-1].targetRoom


def start_game(name):

    player = Player(
        name, 100, 1, 0, weapons["shortsword"],
        rFac.rooms["Living Room"])
    run = True

    while run:
        clearScreen()
        print(
            f"Current Location: ",
            colors.RED,
            f"{player.currentRoom}\n",
            colors.RESET)

        i = 1
        for door in player.currentRoom.doors:
            print(f"[{i}]", door.targetRoom)
            i += 1

        change_location(player, int(input("> ")))

        print("Location: {}".format(player.currentRoom))
