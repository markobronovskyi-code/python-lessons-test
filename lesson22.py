class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.alive = True

goblin = Enemy("Goblin", 30, 5)
orc = Enemy("Orc", 80, 12)

print(goblin.name, "— HP:", goblin.hp, "alive:", goblin.alive)
print(orc.name, "— HP:", orc.hp, "alive:", orc.alive)