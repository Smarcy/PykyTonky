"""Game Actors"""

from pykytonky.misc import clear_screen, Colors


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
    """Player Actor"""

    def __init__(self, name, health, level, experience, weapon, current_room):
        super().__init__(name, health, level, weapon.damage)
        self.experience = experience
        self.weapon = weapon
        self.current_room = current_room

    def print_player_info(self):
        """Display formatted Player Information"""
        clear_screen()
        return(f"Name: {Colors.GREEN}  {self.name}\n{Colors.RESET}"
               f"Health: {Colors.GREEN}{self.health}\n{Colors.RESET}"
               f"Level: {Colors.GREEN} {self.level}\n{Colors.RESET}"
               f"XP: {Colors.GREEN}    {self.experience}\n{Colors.RESET}"
               f"Weapon: {Colors.GREEN}{self.weapon}\n{Colors.RESET}")


class Enemy(Actor):
    """Enemy Actors"""

    def __init__(self, name, health, level, damage, desc):
        super().__init__(name, health, level, damage)
        self.desc = desc
