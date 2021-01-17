"""Create all Items, Weapons etc."""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from model.items import Weapon

weapons = {}

weapons["shortsword"] = Weapon("Shortsword", 10, 3, 100)
weapons["tomahawk"] = Weapon("Tomahawk", 10, 4, 100)
