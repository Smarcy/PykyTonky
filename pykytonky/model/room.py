"""An Actor can only be in a single Room"""


class Room():
    """A Room lol"""

    def __init__(self, name, has_monster):
        self.name = name
        self.has_monster = has_monster
        self.doors = []

    def __str__(self):
        return self.name

    def add_door(self, door):
        """Add a Door to another Room"""
        self.doors.append(door)
