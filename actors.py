class Actor:
    """Base class for all actors"""

    def __init__(self, name, health, level, damage):
        self.name = name
        self.health = health
        self.level = level
        self.damage = damage

    def __str__(self):
        return self.name


class Player(Actor):

    def __init__(self, name, health, level, experience, weapon, currentRoom):
        super().__init__(name, health, level, weapon.get_damage())
        self.experience = experience
        self.weapon = weapon
        self.currentRoom = currentRoom

    def print_player_info(self):
        print(f"\n"
              f"Name:   {self.name}\n"
              f"Health: {self.health}\n"
              f"Level:  {self.level}\n"
              f"XP:     {self.experience}\n"
              f"Weapon: {self.weapon}\n")


class Enemy(Actor):

    def __init__(self, name, health, level, damage, desc):
        super().__init__(name, health, level, damage)
        self.desc = desc
