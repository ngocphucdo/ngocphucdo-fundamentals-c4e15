x = int(input("how many B bacterias are there?"))
t = int(input("how much time in minutes will be wait ?"))
r = x * 2 ** (t//2)
print("After", t, "minutes, we would have", r, "bacterias")
