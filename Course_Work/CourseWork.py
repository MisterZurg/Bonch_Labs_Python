import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math

class File():

    def __init__(self, summ, amount):
        self.summ = summ
        self.amount = amount

    def getAverageValue(self, summ, amount):
        f = open(fname)
        data = []
        data = f.readlines()
        summ = 0.0
        for i in data:
            num = int(i)
            summ += num
            aver = float(summ / len(data))
        print("Average Value: ", aver)
        print("Data: ", data)
        f.close()

    # Completed Task : отметить минимум, максимум
    def minmax(self, summ, amount):
        f = open(fname)
        data = []
        data = f.readlines()
        global min1, max1
        z = 0
        min1 = int(data[0])
        max1 = int(data[0])
        maxi, mini = 0, 0

        for i in data:
            if max1 < int(i):
                max1 = int(i)
                maxi = z
            elif min1 > int(i):
                min1 = int(i)
                mini = z
            z += 1

        plt.plot(mini, min1, 'ro', label='MIN/MAX')
        plt.plot(maxi, max1, 'ro')
        plt.text(maxi, max1, "MAX", fontsize=12, color='RED')
        plt.text(mini, min1, "MIN", fontsize=12, color='RED')

        # Completed Task :вывести экстэмумы ввиде таблицы экстэмумы
        limin = []
        limax = []
        c = 0
        for v in data:
            if int(v) == min1:  # Task.txt
                limin.append(c)
            if int(v) == max1:
                limax.append(c)
            c += 1

        print("Max:", max1, limax, '\n'
                                   "Min:", min1, limin)
        f.close()

    # Completed Task : максимальная скорость изменения графика
    def funcMaxSpeed(self, summ, amount):  # Idea: difference between two values ...
        f = open(fname)
        data = []
        data = f.readlines()
        dataSP = []
        zerodataSP = []
        sp = 0              # Start difference between two values
        sp1 = int(data[0])  # first value
        for i in data:
            if math.fabs(int(sp1 - int(i))) > sp:  # abs of subtraction
                sp = math.fabs(int(sp1 - int(i)))
            sp1 = int(i)

        print("Speed: ", sp)
        sp1 = int(data[0])
        ax = plt.gca()
        for c in range(len(data)):
            if math.fabs(sp1 - int(data[c])) == sp:
                zerodataSP.append(c)
                dataSP.append(int(data[c]))
                l = mlines.Line2D([c - 1, c], [int(data[c - 1]), int(data[c])], color='pink',
                                  linewidth=2.5)  # Dat thing draws a line

                ax.add_line(l)
            sp1 = int(data[c])

        f.close()

    def funcFromFile(self, summ, amount):
        f = open(fname)
        data = []
        data = f.readlines()
        zerodata = []
        c = 0
        for c in range(len(data)):
            data[c] = int(data[c])
            zerodata.append(c)
        plt.plot(zerodata, data, label='UrFuc', color='blue', linewidth=6.0)
        f.close()

    # Completed Task :аппроксимация
    # Completed Task :ввыдо ф - ию аппроксимации
    def funcAproGP(self, summ, amount):

        f = open(fname)

        x, y = [], []

        y = f.readlines()  # y

        for v in range(len(y)):
            x.append(v + 0.001)

            y[v] = int(y[v])

        f.close()

        n = len(x)  # quantity el in lists
        s = sum(y)  # sum of y
        s1 = sum([1 / x[i] for i in range(0, n)])  # sum of 1/x
        s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # sum of (1/x)**2
        s3 = sum([y[i] / x[i] for i in range(0, n)])  # sum of y/x
        a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # factor а with three fractional numbers
        b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # factor b с three fractional numbers
        s4 = [a + b / x[i] for i in range(0, n)]  # list of values of hyperbolic function
        so = round(sum([abs(y[i] - s4[i]) for i in range(0, n)]) / (n * sum(y)) * 100, 3)  # average approximation error

        plt.title('Аппроксимация гиперболой Y=' + str(a) + '+' + str(b) + '/x\n Средняя ошибка--' + str(so) + '%',
                  size=14)
        plt.plot(x, y, color='orange', linestyle=' ', marker='x', label='Data(x,y)')
        plt.plot(x, s4, 'r--', color='g', linewidth=2, label='Data(x,f(x)=a+b/x')
        plt.legend(loc='best')


fname = input('Input Name of the file\n')  # Task.txt
summ, amount = 0.0, 0

Dungeon_Master = File(summ, amount)  # Act of Herritage
Dungeon_Master.getAverageValue(summ, amount)
Dungeon_Master.funcFromFile(summ, amount)
Dungeon_Master.funcMaxSpeed(summ, amount)
Dungeon_Master.minmax(summ, amount)
Dungeon_Master.funcAproGP(summ, amount)

plt.style.use('classic')
plt.xlabel('X label', size=14)  # s_osi
plt.ylabel('Y label', size=14)
plt.legend()                    # Table
plt.show()
