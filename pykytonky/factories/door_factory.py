"""Create all doors in the world"""

from pykytonky.model import door
import pykytonky.factories.room_factory as rFac


def __init__():
    rFac.create_rooms()


def create_doors():
    """obvious"""

    this_door = door.Door(rFac.rooms["Living Room"], rFac.rooms["Hall"])
    this_room = rFac.rooms.get("Living Room")
    this_room.add_door(this_door)

    this_door = door.Door(rFac.rooms["Hall"], rFac.rooms["Living Room"])
    this_room = rFac.rooms.get("Hall")
    this_room.add_door(this_door)

    this_door = door.Door(rFac.rooms["Living Room"], rFac.rooms["Storage"])
    this_room = rFac.rooms.get("Living Room")
    this_room.add_door(this_door)

    this_door = door.Door(rFac.rooms["Storage"], rFac.rooms["Living Room"])
    this_room = rFac.rooms.get("Storage")
    this_room.add_door(this_door)

    this_door = door.Door(rFac.rooms["Hall"], rFac.rooms["Marketplace"])
    this_room = rFac.rooms.get("Hall")
    this_room.add_door(this_door)

    this_door = door.Door(rFac.rooms["Marketplace"], rFac.rooms["Hall"])
    this_room = rFac.rooms.get("Marketplace")
    this_room.add_door(this_door)
