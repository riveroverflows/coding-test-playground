# 반복문 + 메모이제이션

# 초기화
num = int(input())
array = [-1] * (num + 2)

# base case
array[0] = 0
array[1] = 1

# recursive
for i in range(2, num + 1):
    array[i] = array[i - 2] + array[i - 1]

print(array[i])
