"""
1 1 1 1
l r       l + r == m
  l

"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
left, right = 0, 1
while right <= n:
    if left == right:
        right += 1
    curr = sum(nums[left:right])
    print(f"curr: {curr} / left: {left} / right: {right}")
    if curr == m:
        result += 1
        left += 1
        continue
    if curr < m:
        right += 1
        continue
    if curr > m:
        left += 1

print(result)
