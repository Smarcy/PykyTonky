from misc import colors, clearScreen
import factories.room_factory as rFac
import factories.door_factory as dFac
import factories.actor_factory as aFac


def change_location(player, choice):
    player.currentRoom = player.currentRoom.doors[choice-1].targetRoom


def start_game():

    player = aFac.player
    run = True

    while run:
        clearScreen()
        print(
            f"Current Location: ",
            colors.RED,
            f"{player.currentRoom}\n",
            colors.WHITE)

        i = 1
        for door in player.currentRoom.doors:
            print("[{}]".format(i), door.targetRoom)
            i += 1

        change_location(player, int(input("> ")))

        print("Location: {}".format(player.currentRoom))
