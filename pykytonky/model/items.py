"""All kinds of Items in the Game"""

class Item():
    """Base class for all items"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name


class Weapon(Item):
    """Items that have damage and can be equipped"""

    def __init__(self, name, value, damage, condition):
        super().__init__(name, value)
        self.damage = damage
        self.condition = condition

    def __str__(self):
        return super().__str__() + " (Damage: {})".format(self.damage)
