"""
TC: O(n)
- if n < 2: O(n)
- memo = [-1] * (n+1): O(n)
- memo 초기값 할당: O(1)
- for num in range(3, n+1): O(n)
- memo[num-1]+memo[num-2]: O(1)
최종: O(n)

SC: O(n)
memo: O(n)
for num ...: O(1)
최종: O(n)

풀이: 
claude랑 문제 해석해보면서 힌트를 얻어서 풀긴했는데..
n = (n-1)+(n-2) 라는 규칙을 혼자서는 생각해내지 못했을 것 같음..
풀고나서 보니까 피보나치수열 문제 푼거랑 비슷한듯..?
"""

from typing import *
import sys

input = sys.stdin.readline

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        # n = n-1 + n+2
        memo = [-1] * (n+1)
        memo[1] = 1
        memo[2] = 2
        
        for num in range(3, n+1):
            memo[num] = memo[num-1]+memo[num-2]

        return memo[n]


n = int(input())
print(Solution().climbStairs(n))