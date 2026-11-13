class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return 5  # базовий урон

class Slime(Enemy):
    def __init__(self):
        super().__init__("Slime")

    def attack(self):
        return 3

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon")

    def attack(self):
        return 30

monsters = [Slime(), Dragon(), Slime(), Dragon()]
for m in monsters:
    print(f"{m.name} б'є на {m.attack()}")
# Slime б'є на 3
# Dragon б'є на 30
# Slime б'є на 3
# Dragon б'є на 30
