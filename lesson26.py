class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} б'є {self.weapon.name} (урон: {self.weapon.damage})")

sword = Weapon("Меч", 15)
bow = Weapon("Лук", 10)

marko = Player("Marko", sword)
marko.attack()          # Marko б'є Меч (урон: 15)

marko.weapon = bow      # Змінюємо зброю!
marko.attack()          # Marko б'є Лук (урон: 10)
