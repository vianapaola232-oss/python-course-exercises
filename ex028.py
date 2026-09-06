from random import randint
from time import sleep

computer = randint(0,10)

print("\033[33m-=\033[m" * 20)
print(f"\033[34m{'GUESSING GAME':^40}\033[m")
print("\033[33m-=\033[m" * 20)

player = int(input("Please enter a number (between 0 and 10): "))
print("\033[35mPROCESSING...\033[m")
sleep(1)

if player == computer:
    print(f"\033[32mYOU GOT IT!!! You chose {player} and the computer chose {computer}.\033[m")
else:
    print(f"\033[31mDEFEAT!!! You chose {player} and the computer chose {computer}.\033[m")


