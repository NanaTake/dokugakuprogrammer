def power(x):
    """
    Return powered integer.
    :param x: int.
    return x**2.
    """
    return x ** 2

print (power(3))


def print_obj(x):
    """
    Print strings.
    :param x: str.
    """
    print(x)

print_obj('zzz')


def sum_num(x, y, z, a=100, b=1000):
    """
    Sum all numbers.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a=100: int.
    :param b=1000: int.
    sum_num = x + y + z + a + b
    """
    total = x + y + z + a + b
    print(total)

sum_num(1, 2, 3)


def half_num(a):
    """
    Half number and next def.
    :param a: int.
    """
    a = int(a)
    b = a / 2
    print(b)
    return b

def quadruple(b):
    """
    Number * 4.
    :param b: int.
    """
    ans = b * 4
    print(ans)

b = half_num(6)
quadruple(b)

def change_float(a):
    """
    Change str to float.
    :param b: int.
    if b: str , print 'Invalid value.'
    """
    try:
        b = float(a)
        print(b)
        return b
    except ValueError:
        print('Invalid value.')

change_float(3)
