class Enemy:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed

    def info(self):
        print(f"HP: {self.hp}, Speed: {self.speed}")

class FastEnemy(Enemy):
    def __init__(self):
        super().__init__(30, 8)

class StrongEnemy(Enemy):
    def __init__(self):
        super().__init__(100, 2)

e1 = FastEnemy()
e2 = StrongEnemy()
e1.info()    # HP: 30, Speed: 8
e2.info()    # HP: 100, Speed: 2
