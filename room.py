import door
import factories.room_factory


class Room():

    def __init__(self, name, hasMonster):
        self.name = name
        self.hasMonster = hasMonster
        self.doors = []

    def __str__(self):
        return self.name

    def addDoor(self, door):
        self.doors.append(door)
