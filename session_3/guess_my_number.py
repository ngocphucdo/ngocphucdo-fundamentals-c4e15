from random import randint
count = 0

x = randint(1,100)

while True:
    num = int(input("enter a number (1-100): "))
    if num == x:
        print("Bingo")
        break
    elif num < x:
        print("a little too small ")
    else:
        print("a little too big")
    count +=1
    if count >= 7:
        break
