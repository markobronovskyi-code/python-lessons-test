import time
import random

def print_tile(text):
    print(f"==============") 
    time.sleep(0.1)
    print(f"||          ||") 
    time.sleep(0.1)
    print(f"||     {text}    ||") 
    time.sleep(0.1)
    print(f"||          ||") 
    time.sleep(0.1)
    print(f"==============") 

for i in range(6):
    dice = random.randrange(1, 6)
    print_tile(dice)