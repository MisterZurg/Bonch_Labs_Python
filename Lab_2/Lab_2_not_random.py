# Dot coordinates
x = int(input("input X"))
y = int(input("input Y"))
# Line_1
xL1_1 = 0
yL1_1 = 1
xL1_2 = 12
yL1_2 = 8
kL1 = (yL1_1 - yL1_2) / (xL1_1 - xL1_2)
bL1 = yL1_1 - kL1 * xL1_1
# Line_2
xL2_1 = 1
yL2_1 = 0
xL2_2 = 8
yL2_2 = 12
kL2 = (yL2_1 - yL2_2) / (xL2_1 - xL2_2)
bL2 = yL2_1 - kL2 * xL2_1
# Circle
xc = 7
yc = 7
rc = 3

# Comparing inputed data With
if y <= (kL1 * x + bL1):  # Cheking Line_1
    if ((x - xc) ** 2 + (y - yc) ** 2) >= rc ** 2:  # Cheking Circle
        if y <= (kL2 * x + bL2):  # Cheking Under Line_2
            print("Zone 6")
        else:
            print("Zone 8")
    else:
        print("Zone 5")
elif ((x - xc) ** 2 + (y - yc) ** 2) >= rc ** 2:  # Cheking Circle
    if y >= (kL2 * x + bL2):  # Cheking Above Line_2
        print("Zone 1")
    elif 7 <= x <= 12:
        print("Zone 4")
    else:
        print("Zone 7")
else:
    if y >= (kL2 * x + bL2):  # Cheking Above Line_2
        print("Zone 2")
    else:
        print("Zone 3")
