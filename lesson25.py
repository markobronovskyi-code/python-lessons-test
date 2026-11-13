class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self):
        self.x += 5

    def show(self):
        print(f"  [{self.x}, {self.y}, alive={self.alive}]")

    def print(self):
        print(f"hello world "*self.x)

enemies = [Enemy(10, 20), Enemy(50, 20), Enemy(90, 20)]

for e in enemies:
    e.show()

print("--- рухаємо ---")
for e in enemies:
    e.move()

for e in enemies:
    e.show()

enemies[1].alive = False
print("--- видаляємо мертвих ---")
enemies = [e for e in enemies if e.alive]
for e in enemies:
    e.show()  # Лише 2 вороги
    #e.print()