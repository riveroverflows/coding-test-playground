# 재귀 + 메모이제이션


def recursive(n):
    if array[n] != -1:
        return array[n]

    # 메모이제이션 + 재귀
    array[n] = recursive(n - 2) + recursive(n - 1)
    return array[n]


# 초기화
num = int(input())
array = [-1] * (num + 2)

# base case
array[0] = 0
array[1] = 1

print(recursive(num))
