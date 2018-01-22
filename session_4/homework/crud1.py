#1
print("welcome to our shop, what do u want?")
ouritems = ["T-shirt", "Sweater"]
print(*ouritems)
#2
New_item = input("Enter new item: ")
ouritems.append(New_item)
print(*ouritems)
#3
x = int(input("update position?"))
new = input("new item?")
ouritems[x - 1] = new
print(*ouritems, sep=' ')
#4
n = int(input("the position u wanna rid of?"))
ouritems.pop(x - 1)
print(*ouritems, sep=' ')
