nums = [5,7,20,300,60]

num_to_find = int(input("enter a number: "))

for index, num in enumerate(nums):
    if num == num_to_find:
        print("found at index:", index)
        break
else:
    print("not found")
