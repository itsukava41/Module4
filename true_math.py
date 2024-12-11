from math import inf


def divide(first, second):
    if second == 0:
        result = inf
        print(result)
    else:
        result = first / second
        print(f'{first} / {second} =', result)