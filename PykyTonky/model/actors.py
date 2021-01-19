from PykyTonky.misc import clearScreen, colors


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
        clearScreen()
        return(f"Name: {colors.GREEN}  {self.name}\n{colors.RESET}"
               f"Health: {colors.GREEN}{self.health}\n{colors.RESET}"
               f"Level: {colors.GREEN} {self.level}\n{colors.RESET}"
               f"XP: {colors.GREEN}    {self.experience}\n{colors.RESET}"
               f"Weapon: {colors.GREEN}{self.weapon}\n{colors.RESET}")


class Enemy(Actor):

    def __init__(self, name, health, level, damage, desc):
        super().__init__(name, health, level, damage)
        self.desc = desc
