import random

print("\t===  levels  ===\n" \
"\t1 easy\n" \
"\t2 normal\n" \
"\t3 hard\n")

level = int(input("select level: "))
if level == 1:
    secret = random.randint(1, 10)
    print("your level: easy 1-10")
elif level == 2:
    secret = random.randint(1, 50)
    print("your level: normal 1-50")
elif level == 3:
    secret = random.randint(1, 100)
    print("your level: hard 1-100")


tries=0
while True:
    guess=int(input("your guess: "))
    tries += 1


    if guess == secret:
        print(f"Ти вгадав за {tries} спроби!")
        break
    elif guess > secret:
        print("Менше!")
    elif guess < secret:
        print("Більше!")
        