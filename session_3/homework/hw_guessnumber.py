from random import randint
x = randint(1, 100)
l = print("your guess larger than my number")
s = print("your guess smaller than my number")
c = print("correct")
hint = input("s/l/c")
print("is", x, "your number?")
if hint== "l": x = randint (1, x)
elif hint== "s": x = randint(x+1, 100)
elif hint== "c":
    print("correct")
