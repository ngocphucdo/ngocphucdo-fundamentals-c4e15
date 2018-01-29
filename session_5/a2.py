nums = [7, 5, 10, 8, 200, 30]

num_to_find = int(input("enter a number: "))

#1. gia dinh ket qua
found_index = -1 #not found

#2. create a loop to test our assumption
for index, num in enumerate(nums):
    if num == num_to_find:
        found_index = index #update gia dinh
        break
#3. print results
if found_index == -1:
    print("not found")
else:
    print("found at index", found_index)
