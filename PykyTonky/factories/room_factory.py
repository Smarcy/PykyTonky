import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from model import room

rooms = {}


def createRooms():
    rooms["Living Room"] = room.Room("Living Room", False)
    rooms["Hall"] = room.Room("Hall", False)
    rooms["Marketplace"] = room.Room("Marketplace", True)
    rooms["Storage"] = room.Room("Storage", True)
