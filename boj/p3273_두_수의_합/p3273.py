import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()
result = 0
left, r = 0, n - 1
count = 0
while left < r:
    count += 1
    print(f"count: {count}")
    curr = nums[left] + nums[r]
    if curr == target:
        result += 1
        left += 1
        continue
    if curr < target:
        left += 1
        continue
    if curr > target:
        r -= 1

print(result)
