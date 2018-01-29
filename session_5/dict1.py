teencode = {
    "ng" : "Nguoi, Noi ve con nguoi, mot nguoi nao do hoac noi chung ve loai nguoi",
    "pt" : "phat trien,... phat trien mot cai gi do",
    "clgt": "cau lam gi the",
    "nn" : "ngu ngon"
}
loop = True
while loop:
    for key in teencode:
        print(key, end=' ')
    print()
    x = input("Enter a code:")
    if x in teencode:
        print(teencode[x])
    elif x == "exit":
        break
    else:
        print("not found")
        y = input("not found, do u want to update this word?(yes/no)")
        if y == "yes":
            c = input("what this word mean?")
            teencode[x] = c
        print(*teencode)
