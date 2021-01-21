"""A Door connects one Room with another"""

class Door():
    """A Door lol"""

    def __init__(self, source_room, target_room):
        self.source_room = source_room
        self.target_room = target_room

    def __str__(self):
        return self.target_room
