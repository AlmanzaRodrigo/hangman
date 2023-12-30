import time
from os import system
from hangman_message import MESSAGE


def animation():
    i = 14
    for x in range(1, 2):
        system("cls")
        print(MESSAGE[i])
        i += 1
        time.sleep(0.4)
        system("cls")
        print(MESSAGE[i])
        i -= 1
        time.sleep(0.4)
        system("cls")
        print(MESSAGE[i])
        i += 2
        time.sleep(0.4)
        system("cls")
        print(MESSAGE[i])
        i -= 2
        time.sleep(0.4)
    for veces in range(1, 6):
        system("cls")
        print(MESSAGE[veces + 8])
        time.sleep(0.4)


