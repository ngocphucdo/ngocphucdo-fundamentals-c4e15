from getpass import getpass
count = 0

while True:
    username = input("username ")
    password = getpass("password ")

    if username == "c4e":
        if password == "techkids":
            print ("chao mung den he thong")
            break
        else:
            print ("sai password")
    else:
        print ("sai username")
    count += 1
    if count >=3:
        print("You filed to log 3 times, go away")
        break
