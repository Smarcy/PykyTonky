from misc import clearScreen
import factories.room_factory as rFac
import factories.door_factory as dFac
import factories.actor_factory as aFac


def change_location(choice):
    aFac.player.currentRoom = aFac.player.currentRoom.doors[choice-1].targetRoom


def start_game():
    run = True

    while run:
        clearScreen()
        print("Welcome to ApplePy!\n")

        i = 1
        for door in aFac.player.currentRoom.doors:
            print("[{}]".format(i), door.targetRoom)
            i += 1

        change_location(int(input("> ")))

        print("Location: {}".format(aFac.player.currentRoom))
        input()
