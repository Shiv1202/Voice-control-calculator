def fact(num):
    val = num[0]

    dp = [0] * (val + 1)
    dp[0] = 1
    for i in range(1, val + 1):
        dp[i] = dp[i - 1] * i
    return dp[val]

# print((fact([5])))