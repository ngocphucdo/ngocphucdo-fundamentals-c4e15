digits = 0
n = int(input("enter a number: "))

while n > 0:
    n = n // 10
    digits += 1
print(digits)
