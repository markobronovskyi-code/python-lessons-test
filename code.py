import os
import random

games = ["minecraft", "fortnite", "quake||", "quake|"]
state_file = "last_game.txt"

previous_game = None
if os.path.exists(state_file):
    with open(state_file, "r", encoding="utf-8") as f:
        previous_game = f.read().strip()

chosen_game = random.choice(games)
while previous_game is not None and chosen_game == previous_game and len(games) > 1:
    chosen_game = random.choice(games)

with open(state_file, "w", encoding="utf-8") as f:
    f.write(chosen_game)

print(f"=== todays mission ===\n"
      f"\t{chosen_game}\n"
      f"\t\n"
      f"\t\n"
      f"\t\n"
      f"\t")