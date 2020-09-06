def add(num):
    return sum(num)


def sub(num):
    ans = num[0]
    for i in range(1, len(num)):
        ans -= num[i]
    return ans

def multiply(num):
    ans = num[0]
    for i in range(1, len(num)):
        ans *= num[i]
    return ans

def divide(num):
    res = num[0] / num[1]
    if int(res) == res:
        return int(res)
    return res
