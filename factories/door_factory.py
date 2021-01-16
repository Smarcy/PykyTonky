import door
import factories.room_factory as rFac


def __init__():
    rFac.createRooms()


def createDoors():

    thisDoor = door.Door(rFac.rooms["Living Room"], rFac.rooms["Hall"])
    thisRoom = rFac.rooms.get("Living Room")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door(rFac.rooms["Hall"], rFac.rooms["Living Room"])
    thisRoom = rFac.rooms.get("Hall")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door(rFac.rooms["Living Room"], rFac.rooms["Storage"])
    thisRoom = rFac.rooms.get("Living Room")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door(rFac.rooms["Storage"], rFac.rooms["Living Room"])
    thisRoom = rFac.rooms.get("Storage")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door(rFac.rooms["Hall"], rFac.rooms["Marketplace"])
    thisRoom = rFac.rooms.get("Hall")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door(rFac.rooms["Marketplace"], rFac.rooms["Hall"])
    thisRoom = rFac.rooms.get("Marketplace")
    thisRoom.addDoor(thisDoor)
