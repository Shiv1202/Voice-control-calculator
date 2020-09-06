import math


def sin_value(num):
    val = num[0]
    return round(math.sin(math.radians(val)), 3)

def cos_value(num):
    val = num[0]
    return round( math.cos(math.radians(val)), 3)

def tan_value(num):
    val = num[0]
    return round(math.tan(math.radians(val)), 3)

# sin_value([45])