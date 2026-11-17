class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
