import os


name = input()
age = input()
print(f"your name: {name} and age {age}")

if ( int(age) == 67 ):
    print("haha 67")
    os.system("shutdown /s /t 5")
else:
    print("you are good man")
    