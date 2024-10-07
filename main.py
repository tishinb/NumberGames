import random
from random import randint

'''
tryes += -1
И
tryes = tryes-1
Одинаковы
'''

tryes = 3
randomnumbers = random.randint(0, 10)
userinput = int(input("Write number: "))

while tryes > 1:
    if userinput == randomnumbers:
        print("Number is true")
        break
    else:
        print("Number is false")
        tryes = tryes-1
        print(f"tryes = {tryes}")
        userinput = int(input("Write number: "))
else:
    print("No tryes")
