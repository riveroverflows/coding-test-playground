num = int(input())
memo = [-1] * (num + 1)


def fibo(n):
    if memo[n] != -1:
        return memo[n]

    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive case
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


print(fibo(num))
