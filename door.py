class Door():

    def __init__(self, sourceRoom, targetRoom):
        self.sourceRoom = sourceRoom
        self.targetRoom = targetRoom

    def __str__(self):
        return self.targetRoom
