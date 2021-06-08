import math
from decimal import (
    Decimal,
    getcontext
)

def is_square(n):
    is_square = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n == i ** 2:
            is_square = True
            break
    return is_square

def get_sqrt(D):
    getcontext().prec = 100
    x = int(D)
    for i in range(20):
        x = Decimal(str(x - (x ** 2 - D) / (2 * x)))
    return x

def get_continued_fraction(D):
    continued_fraction = []
    if not is_square(D):
        y = get_sqrt(D) - int(get_sqrt(D))
        continued_fraction.append(int(1 / y))
        z = 1 / y - int(1 / y)
        while True:
            if abs(y - z) < 1e-5:
                break
            else:
                continued_fraction.append(int(1 / z))
                z = 1 / z - int(1 / z)
    return continued_fraction

def get_minimal_solution(D):
    continued_fraction = get_continued_fraction(D)
    length = len(continued_fraction)
    num = length % 2 + 1
    continued_fraction = continued_fraction * num
    an2, bn2 = 0, 0
    an1, bn1 = 0, 0
    an, bn = 1, 0 

    for n in range (1, num * length + 1):
        if n == 1:
            an1, bn1 = int(math.sqrt(D)), 1
        else:
            an2, bn2 = (an + continued_fraction[n - 2] * an1,
                        bn + continued_fraction[n - 2] * bn1)
            an, bn = an1, bn1
            an1, bn1 = an2, bn2
    print_continued_fraction = continued_fraction[:int(len(continued_fraction) / num)]
    print_continued_fraction.insert(0, int(get_sqrt(D)))
    print('連分数展開: {}'.format(print_continued_fraction))
    return an2, bn2

if __name__ == '__main__':
    d = 2
    x, y = get_minimal_solution(d)
    print('最小解\n  x: {}\n  y: {}'.format(x, y))
