class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def is_alive(self):
        return self.hp > 0

hero = Player("Marko", 50)
print(hero.hp, hero.is_alive())   # 50 True

hero.take_damage(30)
print(hero.hp, hero.is_alive())   # 20 True

hero.take_damage(20)
print(hero.hp, hero.is_alive())   # 0 False
def show_status():
    print(f"{hero.name} HP: {hero.hp}")
show_status()
