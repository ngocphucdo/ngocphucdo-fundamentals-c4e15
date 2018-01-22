print("Hi, my name is Phuc and there're my ship sizes: ", ["5","7","300","90","24","50","75"])
ship_sizes = [5,7,300,90,24,50,75]

for i in range(4):
    print("Month{0}".format(i+1))
    biggest = max(ship_sizes)
    print("Now my biggest sheep has size {0} let's shear it".format(biggest))
    print("After shearing, here is my flock")
    ship_sizes[ship_sizes.index(biggest)] = 8
    print(ship_sizes)
    print("One month has passed, now here is my flock")
    for i in range(7):
        x = ship_sizes[i]
        ship_sizes[i] = x + 50
    print(ship_sizes)
    total = sum(ship_sizes)
    print(total)
print("My flock has size in total: ",total)
abc = total*2
print("I would get", abc,"$")
