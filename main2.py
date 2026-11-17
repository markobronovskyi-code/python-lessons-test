from player import Player

player = Player(200, 150)
player.move(5, 0)
print(f"Player at ({player.x}, {player.y}), HP: {player.hp}")
# Player at (205, 150), HP: 100