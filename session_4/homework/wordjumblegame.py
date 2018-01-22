import random
words = ("champion","python","phuongbui",'love')
play=input("Do you want to play? (yes or no)")
while play=="yes":
    word = random.choice(words)
    correct = word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    print("The jumble is:", jumble)

    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        guess = input("Your guess: ")

    if guess == correct:
        print("That's it!  You guessed it!\n")
        break
    elif guess== "":
        print("You failed...")
