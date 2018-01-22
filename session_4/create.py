print("hi there, here your favorite things so far")
menu = ["Phuong Bui", "basketball", "my brothers"]
print(*menu, sep=' ')

new_far = input("name one thing u want to add?")
menu.append(new_far)

print(*menu, sep=' ')
