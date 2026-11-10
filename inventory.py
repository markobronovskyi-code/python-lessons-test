import random

loot = ["sword", "shield", "potion", "gold", "magic ring"]
item = random.choice(loot)
item1 = random.choice(loot)
item2 = random.choice(loot)
print(f"you found: {item} and {item1} and {item2}")
inventory = []
inventory.append(item)
inventory.append(item1)
inventory.append(item2)
print("\t===  items  ===\n"
f"\t{inventory}\n")