"""Create all Player, Enemy and NPC Objects"""

# import factories.item_factory as iFac
import actors


def createPlayer(name, health, level, exp, weapon, currentRoom):
    global player
    player = actors.Player(name, health, level, exp, weapon, currentRoom)
    return player

def getPlayer():
    return player
