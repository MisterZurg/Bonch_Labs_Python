import random
# Dot coordinates
x = int(input("input X"))
y = int(input("input Y"))
# Degeneration of zones
# Line
xL_1 = random.randint(0, 20)
yL_1 = random.randint(0, 20)
xL_2 = random.randint(0, 20)
yL_2 = random.randint(0, 20)
kL = (yL_1 - yL_2) / (xL_1 - xL_2)
bL = yL_1 - kL * xL_1
# Circle
xc = random.randint(0, 20)
yc = random.randint(0, 20)
rc = random.randint(0, 20)
# Rectangle Need Help
xR_1 = random.randint(0, 20)
yR_1 = random.randint(0, 20)
xR_2 = random.randint(0, 20)
yR_2 = random.randint(0, 20)
# Comparing
if (y > kL * x + bL):
   if ((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2):
       print("Zone_1")
   elif (xL_1 < x < xL_2) and (yL_1 < y < yL_2):
       print("Zone_3")
   else:
       print("Zone_2")
elif ((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2):
   if (xL_1 < x < xL_2) and (yL_1 < y < yL_2):
       print("Zone_7")
   else:
       print("Zone_8")
elif (xL_1 < x < xL_2) and (yL_1 < y < yL_2):
   print("Zone_4")
elif y > yL_2:
   print("Zone_7")
else:
   print("Zone_8")
