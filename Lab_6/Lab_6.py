class Elevator():
    """Флекс"""

    # Method
    def __init__(self, ourpos, lfpos, doors):
        self.ourpos = ourpos
        self.lfpos = lfpos
        self.doors = doors

    """def inputParametrs(self, ourpos, lfpos, doors):
        self.ourpos, self.lfpos, self.doors = int(input("input Human position")), float(
            input("input Lift position")), int(
            input("input Dorrs\n1 closed / 0 opend"))"""

    # Ля а как оно работает

    def getCondition(self, ourpos, lfpos, doors):
        print('Мы ВЫЗЫВАЕМ лифт')
        if self.ourpos == self.lfpos:
            if self.doors == 0:
                print('Лифт уже на вашем этаже')
            else:
                print('Лифт сломан на вашем этаже')
        elif int(self.lfpos) != self.lfpos:
            if self.doors == 0:  # 1 closed / 0 opend
                print('Лифт в шоколадной шахте, едет с открыми дверьми с этажа', Lift.lfpos, 'на', Lift.ourpos)
            else:
                print('Лифт в шоколадной шахте, едет с закрытыми дверьми с этажа', Lift.lfpos, 'на', Lift.ourpos)
        else:
            if self.doors == 0:
                print('Лифт сломан, едет с открыми дверьми с этажа', Lift.lfpos, 'на', Lift.ourpos)
            else:
                print('Лифт работает, едет с закрытыми дверьми с этажа', Lift.lfpos, 'на', Lift.ourpos)


ourpos, lfpos, doors = int(input("input Human position")), float(input("input Lift position")), int(
    input("input Dorrs\n1 closed / 0 opend"))
Lift = Elevator(ourpos, lfpos, doors)
Lift.getCondition(ourpos, lfpos, doors)

print(Lift.ourpos, Lift.lfpos, Lift.doors)
