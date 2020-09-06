import math

def find_sqrt(num):
    x = math.sqrt(num[0])
    return x if int(x) == x else x


def power(num):
    if len(num) < 2:
        return "Please input both base and power for calculation."
    x, n = num[0], num[1]
    if n == 0:
        return 1
    temp = x ** (n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x

def square(num):
    x = num[0]
    return power([x, 2])

def cube(num):
    x = num[0]
    return power([x, 3])

def cube_root(num):
    digit = num[0]
    return math.pow(digit, 1/3)