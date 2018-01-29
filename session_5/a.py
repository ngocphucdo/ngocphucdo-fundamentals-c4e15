#tao 1 list (int)
#Hoi nguoi dung nhap vao 1 so
#Noi cho nguoi dung biet so nay co ton tai trong day khong, neu co thi index la bao nhieu?

nums = [1,2,5,7,9]

num_to_find = int(input("enter a number: "))

if num_to_find in nums:
    print("Found")
    found_index = nums.index(num_to_find)
    print("Index:", found_index)
else:
    print("Not Found")
