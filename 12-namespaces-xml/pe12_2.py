import time

b = 7


def verdubbel_b():
    global b
    b = b + b


verdubbel_b()

print(b)


print(time.strftime("%H:%M:%S"))


def f(y):
    return 2 * y + 1


def g(x):
    return 5 + x + 10


print(f(3) + g(3))
