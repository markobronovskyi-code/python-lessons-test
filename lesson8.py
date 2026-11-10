# import random

# for i in range(random.randrange(3)+3):
#     damage=random.randint(1, 20)
#     if damage>=(18):
#         print(f"critical hit!{damage}")
#     else:
#         print(damage)

import random

secret = random.randint(1, 20)
tries=0
while True:
    guess = int(input("Твоя відповідь: "))

    tries += 1

    if secret>guess:
        print("Більше!")
    elif secret<guess:
        print("Менше!")
    elif secret==guess:
        print(f"Ти вгадав за {tries} спроби!")
        break

