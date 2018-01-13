yob = int(input("Your year of birth?"))
age = 2018 - yob
print("Your age is", age)

if age < 10:
    print("Baby")
elif age < 18:
    print("teenager")
else:
    print("adult")
