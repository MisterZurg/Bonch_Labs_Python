import math

a = float(input('input_a'))
b = float(input('input_b'))
c = float(input('input_c'))
if a != 0:
    D = b * b - 4 * a * c
    if D > 0:
        x1 = -b + math.sqrt(D) / 2 * a
        x2 = -b - math.sqrt(D) / 2 * a
        if x1 != x2:
            print('2 solutions x1=', x1, 'x2=', x2)
        else:
            print('2 similar solutions x1=x2', x1)
    elif D == 0:
        x1 = - b / 2 * a
        print('1 solution x1', x1)
    else:
        print('none')
else:
    if b != 0:
        x1 = -b / c
        print('x=', x1)
    else:
        if c != 0:

            print('none')
        else:
            print('Any of x')
