import random

n = int(input('InputAmountOfStrings\n'))
myNumList = []
j = 1
for r in range(n):  # n строк
   myNumList.append([])  # создаем пустую строку
   for c in range(12):   # в каждой строке - 12 элементов
       rnd = random.randint(0, 100)
       myNumList[r].append(rnd)  # добавляем очередной элемент в строку
       min = 10000
       for i in myNumList[r - 1]:
           for j in myNumList[r]:
               if i * j <= min:
                   min = i * j
   print(myNumList[r], "MinMultiply: ", min)
