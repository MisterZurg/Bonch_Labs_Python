import random

n = int(input('InputAmountOfStrings'))
anal = []
for r in range(n):  # n строк
    anal.append([])  # создаем пустую строку
    min1, min2, mx, maxi = 101, 101, -1, 0
    for c in range(12):  # в каждой строке - 12 элементов
        rnd = random.randint(0, 100)
        anal[r].append(rnd)  # добавляем очередной элемент в строку
        if rnd < min1:
            min2, min1 = min1, rnd
        elif rnd < min2:
            min2 = rnd
        if rnd > mx:
            mx, maxi = rnd, c
    print(anal[r], 'm1=', min1, 'm2=', min2, 'MinMul=', min1 * min2)
    print('mx=', mx, 'ind=', maxi)
print("Tupo pagiloй Массив")
for r in range(n):  # n строк
    emax, iemax, esw = 0, 0, 0
    for c in range(12):
        if anal[r][c] > emax:
            emax, iemax = anal[r][c], c
    esw, anal[r][r], anal[r][iemax] = anal[r][r], emax, esw
    print(anal[r], 'Swaped=', esw, emax)
print("Tupo redhead && mustang")
# Gnome sort
i, j = 1, 2
while i < n:
    if anal[i - 1][i - 1] < anal[i][i]:  # min < max
        i, j = j, j + 1
    else:
        tmp, anal[i - 1][i - 1], anal[i][i] = anal[i - 1][i - 1], anal[i][i], tmp
        i = i - 1
        if i == 0:
            i, j = j, j + 1
for r in range(n):
    print(anal[r], anal[r][r])
