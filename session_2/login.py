from getpass import getpass


username = input("username ")
password = getpass("password ")

if username == "c4e":
        if password == "techkids":
            print ("chao mung den he thong")
        else:
            print ("sai password")
else:
    print ("sai username")
