# x=1

# while x < 10:
#     print(x)
#     x += 1
import time
import os

x=10

while x >= 1:
    print(x)
    x -= 1
    time.sleep(1)
if x == 0:
    print("boom!!")
    response = input("do you want to turn your pc off (yes/no)? ")
    if response =="no":
       print("ok")
    if response =="yes":
     os.system("shutdown /s /t 0.1")
    else :
       print("Try again")