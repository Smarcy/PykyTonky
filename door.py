class Door():

    def __init__(self, name, sourceRoom, targetRoom):
        self.name = name
        self.sourceRoom = sourceRoom
        self.targetRoom = targetRoom

    def __str__(self) -> str:
        return self.name
