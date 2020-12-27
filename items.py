class Item():

    """Base class for all items"""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "Name: {}, Value: {}".format(self.name, self.value)


class Weapon(Item):

    def __init__(self, name, value, damage):
        super().__init__(name, value)
        self.damage = damage

    def __str__(self):
        return super().__str__() + " Damage: {}".format(self.damage)
