count = 0
while True:
    yob = int(input("your year of birth "))
    age = 2018 - yob

    if age < 10:
        print("baby")
    elif age < 18:
        print("teenager")
    else:
        print("adult")
    count += 1
    if count >= 5:
        break
