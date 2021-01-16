import door
import factories.room_factory


def __init__():
    factories.room_factory.createRooms()


def createDoors():

    thisDoor = door.Door("LivingRoomToHall", "Living Room", "Hall")
    thisRoom = factories.room_factory.rooms.get("Living Room")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door("HallToLivingRoom", "Hall", "Living Room")
    thisRoom = factories.room_factory.rooms.get("Hall")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door("LivingRoomToStorage", "Living Room", "Storage")
    thisRoom = factories.room_factory.rooms.get("Storage")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door("StorageToLivingRoom", "Storage", "Living Room")
    thisRoom = factories.room_factory.rooms.get("Living Room")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door("HallToMarketPlace", "Hall", "Marketplace")
    thisRoom = factories.room_factory.rooms.get("Hall")
    thisRoom.addDoor(thisDoor)

    thisDoor = door.Door("MarketplaceToHall", "Marketplace", "Hall")
    thisRoom = factories.room_factory.rooms.get("Marketplace")
    thisRoom.addDoor(thisDoor)
