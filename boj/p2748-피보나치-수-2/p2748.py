def recursive(num: int) -> int:
    if fibo[num] != -1:
        return fibo[num]
    fibo[num] = recursive(num - 1) + recursive(num - 2)
    return fibo[num]


n = int(input())
fibo = [-1] * (n + 2)

fibo[0] = 0
fibo[1] = 1

print(recursive(n))
