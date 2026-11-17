class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.hp = 100

    def attack(self, enemy):
        enemy.hp -= self.weapon.damage
        print(f"{self.name} б'є {self.weapon.name} → {enemy.name}: {enemy.hp} HP")

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class FastEnemy(Enemy):
    def __init__(self):
        super().__init__("FastBat", 30)

sword = Weapon("Меч", 25)
hero = Player("Marko", sword)
bat = FastEnemy()

hero.attack(bat)   # Marko б'є Меч → FastBat: 5 HP