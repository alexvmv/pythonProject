numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def func(i):
    if i % 2 != 0 and i > 50:
        return 1


print(list(filter(func, numbers)))
