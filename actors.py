class Actor():
    """Base class for all actors"""

    def __init__(self, name, health, desc, weapon):
        """test"""
        self.name = name
        self.health = health
        self.desc = desc
        self.weapon = weapon

    def __str__(self):
        """test"""
        return self.name

class Player(Actor):
    """Player class"""

class Enemy(Actor):
    """Enemy class"""
