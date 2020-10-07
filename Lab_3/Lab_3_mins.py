import random

n = int(input('InputAmountOfStrings\n'))
myNumList = []
j = 1
for r in range(n):  # n строк

   myNumList.append([])  # создаем пустую строку
   for c in range(12):  # в каждой строке - 12 элементов
       rnd = random.randint(0, 100)
       myNumList[r].append(rnd)  # добавляем очередной элемент в строку])

for r in range(n):  # n строк [[],[],[]] ansl[][]
   min1 = 101
   min2 = 101
   for c in range(12):
       if myNumList[r][c] <= min1:
           min2 = min1
           min1 = myNumList[r][c]
   print(myNumList[r], "m1=", min1, "m2=", min2)
