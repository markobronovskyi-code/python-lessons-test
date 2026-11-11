import os
level = int(input("Enter your level: "))
coins = int(input("Enter your coins: "))
has_key = input("Do you have a key? (yes/no): ")
if has_key.lower() == "yes" and level > 5 and coins >= 100 and coins < 500:
    print("You can enter the dungeon!")
if coins == 500:
    print("cheater")
