"""Create all Player, Enemy and NPC Objects"""

import factories.item_factory as iFac
import actors


def getPlayer():
    return actors.Player("Smarc", 100, 1, 0, iFac.weapons["shortsword"])
