pairs = []

for i in range(5):
    if i == 0:
        pairs.append(1)
    elif i == 1:
        pairs.append(2)
    else:
        pairs.append(p[i-1] + p[i-2])
    print("Month {0}: {1} pair(s) of rabbits".format(i,pairs[i]))
