numbers = [1, 6, 8, 1, 2, 1, 5, 6]

n = int(input("enter a number: "))

x = 0
for i, num in enumerate(numbers):
    if n in numbers and num == n:
        x +=1


print(n, "appears", x, "times at my list")
