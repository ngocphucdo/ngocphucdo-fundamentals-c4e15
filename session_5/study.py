st = input("write st:").lower()


letter_count = {}
for letter in st:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for key, value in letter_count.item():
    print(key, value)
