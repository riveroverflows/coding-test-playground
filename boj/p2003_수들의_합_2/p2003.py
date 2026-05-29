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
l, r = 0, 1
while r <= n:
    if l == r:
        r += 1
    curr = sum(nums[l:r])
    print(f"curr: {curr} / left: {l} / right: {r}")
    if curr == m:
        result += 1
        l += 1
        continue
    if curr < m:
        r += 1
        continue
    if curr > m:
        l += 1

print(result)
