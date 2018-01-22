# menu = ["Pho", "Thit cho", "Tieu ho"]
# menu.pop(0) #cach1
# # menu.remove("Thit cho") #cach2
print("hi there, here your favorite things so far")
menu = ["Phuong Bui", "basketball", "my brothers"]

for index, item in enumerate(menu):
    print(index +1, item)

pos = int(input("the position u wanna rid of {}".format(item)))

menu.pop(pos-1)

print(menu)
