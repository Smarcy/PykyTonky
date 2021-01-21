"""Create all rooms in the world"""

from pykytonky.model import room

rooms = {}


def create_rooms():
    """obvious"""
    rooms["Living Room"] = room.Room("Living Room", False)
    rooms["Hall"] = room.Room("Hall", False)
    rooms["Marketplace"] = room.Room("Marketplace", True)
    rooms["Storage"] = room.Room("Storage", True)
