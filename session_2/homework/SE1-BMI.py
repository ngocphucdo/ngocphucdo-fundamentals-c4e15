Mass = int(input("Your mass = "))
Height = int(input("Your Height = "))

BMI = Mass / (Height*Height / 10000)
print("BMI", BMI)

if BMI < 16 :
    print("Severely underweight")
if 16 < BMI < 18.5:
    print("Underweight")
if 18.5 < BMI < 25:
    print("Normal")
if 25 < BMI < 30:
    print("Overweight")
if BMI > 30:
    print("Obese")
