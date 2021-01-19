"""Create all Items, Weapons etc."""

from PykyTonky.model.items import Weapon

weapons = {}

weapons["shortsword"] = Weapon("Shortsword", 10, 3, 100)
weapons["tomahawk"] = Weapon("Tomahawk", 10, 4, 100)
