class Actor:
    """Base class for all actors"""

    def __init__(self, name, health, level, weapon):
        self.name = name
        self.health = health
        self.level = level
        self.weapon = weapon

    def __str__(self):
        return self.name


class Player(Actor):

    def __init__(self, name, health, level, experience, weapon):
        super().__init__(name, health, level, weapon)
        self.experience = experience

    def printPlayerInfo(self):
        print(f"Name: {self.name}\n"
              f"Health: {self.health}\n"
              f"Level: {self.level}\n"
              f"XP: {self.experience}\n"
              f"Weapon: {self.weapon}\n")


class Enemy(Actor):

    def __init__(self, desc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.desc = desc
