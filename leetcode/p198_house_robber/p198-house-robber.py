"""
TC: O(n), SC: O(n)

n은 nums 리스트의 길이.

풀이:
- 첫번째 접근: 순회하면서 이전집을 털었는지 안털었는지 확인하고 털었으면 건너뛴다는 생각을 해봄
  - claude 피드백: 건너뛴다/안뛴다가 아니라 턴다/안턴다로 봐야함.
- 두번째 접근: i-1, i+1 확인하고 안털었으면 더 큰걸 턴다
  - claude 피드백: 그건 greedy 접근법. 그렇게 풀면 최적해를 구할 수 없음. DP방식으로 풀어야함. nums[i-1]의 최댓값과 (현재값+nums[i-2]최댓값) 중에 큰 걸 선택하면 하나씩 건너뛰고 선택하게됨.
  - DP: 큰 문제를 작은 하위 문제로 쪼개서 이전 결과를 저장해가며 푸는 기법
- 세번째 접근: claude 피드백에서 정답에 가까운 힌트를 얻고 풀게됨. 코드는 지저분했지만 통과했고 이후 코드 개선까지 완료.
  1. nums 길이 만큼의 memo 배열을 생성. memo는 nums의 인덱스 별 최댓값을 저장함
  2. nums 순회
  3. index 0, 1 초기값 설정
  4. nums[i-1]의 최댓값 memo[i-1]와 (현재 값 num + nums[i-2]의 최댓값 memo[i-2])를 비교하고 더 큰 값을 memo[i]에 저장
  5. memo의 마지막 인덱스를 리턴

TC:
- memo 배열 생성: O(n).
- nums 순회: O(n). 각 단계에서 비교/대입은 O(1).
- 종합: O(n).

SC:
- memo(list): 크기 n. O(n).
- i, num: 각 O(1).
- 종합: O(n).
"""

from typing import List
import json


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                memo[0] = nums[0]
                continue
            if i == 1:
                memo[1] = max(nums[0], nums[1])
                continue

            memo[i] = max(memo[i-1], num + memo[i-2])

        return memo[-1]


nums = json.loads(input())
print(Solution().rob(nums))