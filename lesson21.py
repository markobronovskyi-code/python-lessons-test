class Monster:
    pass

goblin = Monster()
goblin.name = "Goblin"
goblin.hp = 30

dragon = Monster()
dragon.name = "Dragon"
dragon.hp = 200

print(goblin.name, "має", goblin.hp, "HP")
print(dragon.name, "має", dragon.hp, "HP")

goblin.hp = 0
print(goblin.name, "має", goblin.hp, "HP")
print(dragon.name, "має", dragon.hp, "HP")  # Dragon не змінився!
