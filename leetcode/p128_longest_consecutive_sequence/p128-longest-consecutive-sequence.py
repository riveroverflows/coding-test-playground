"""
Longest Consecutive Sequence (LeetCode 128, Medium)

정렬되지 않은 정수 배열 nums가 주어질 때,
가장 긴 연속 수열(consecutive sequence)의 길이를 반환하라.
O(n) 시간복잡도로 풀어야 한다.

Example 1:
  Input: nums = [100, 4, 200, 1, 3, 2]
  Output: 4
  Explanation: 1, 2, 3, 4 → 길이 4

Example 2:
  Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
  Output: 9
  Explanation: 0, 1, 2, 3, 4, 5, 6, 7, 8 → 길이 9

Constraints:
  0 <= nums.length <= 10^5
  -10^9 <= nums[i] <= 10^9
"""

import json
from typing import List

"""
TC: O(n), SC: O(n)

n은 nums 리스트의 길이.

풀이과정:
- nums를 set으로 만드는 것까진 알겠는데 이후로 풀이가 이어지지 않았음
- 여러 풀이 방법을 시도해보다가 도저히 생각나지 않아서 LeetSub 플러그인 힌트 4/5까지 봄
- "num - 1이 set에 없다면 sequence의 시작 숫자일 수 있다"에서 힌트를 얻어서 풀게 됨

풀이:
- set에 넣어서 O(1) 조회할 수 있도록 함
- set에 num-1 값이 있다면 num은 sequence의 시작 숫자가 아니므로 skip
- 시작 숫자에서 cnt(+1, +2, +3, ...)를 더해가며 set에 있는지 확인
- answer와 cnt 중 더 큰 값을 answer에 저장

TC:
- set(nums): n개 원소 삽입. O(n).
- for num in nums_set: set 전체 순회. O(n).
  - if num - 1 in nums_set: 해시 기반 조회. O(1).
  - while: 시작 숫자에서만 실행. for-while 중첩이라 O(n²)처럼 보이지만,
    각 원소는 while에서 최대 1번만 방문됨. 전체 while 반복 합계 = O(n).
- 종합: O(n).

SC:
- nums_set: 최악 n개 원소. O(n).
- answer, cnt: 상수. O(1).
- 종합: O(n).
"""
def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    answer = 0

    for num in nums_set:
        if num - 1 in nums_set:
            continue
        cnt = 0
        while num + cnt in nums_set:
            cnt += 1
        answer = max(answer, cnt)

    return answer

a = json.loads(input())
print(longestConsecutive(a))

    

