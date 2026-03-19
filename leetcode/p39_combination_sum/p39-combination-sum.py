"""
TC: O(N^(T/M))
    - N = len(candidates), T = target, M = min(candidates)

    [왜 N^(T/M)인가?]
    1. 최대 깊이 = T/M
       - 재귀가 한 단계 깊어질 때마다 path_sum에 candidate를 더함
       - candidate는 항상 >= M (최소 후보값)
       - 따라서 깊이 d에서 path_sum >= d * M
       - path_sum > target이면 return하므로, d * M > T이면 반드시 종료
       - 즉, 재귀는 깊이 ⌈T/M⌉을 절대 넘을 수 없음
       - 예: candidates=[2,3,6,7], target=7 → ⌈7/2⌉ = 4

    2. 각 깊이에서 최대 N개 분기
       - for i in range(start, len(candidates))가 최대 N번 반복
       - 각 반복마다 backtrack()을 재귀 호출 → 자식 노드 최대 N개
       - depth 0: 1개, depth 1: N개, depth 2: N^2개, ..., depth d: N^d개
       - 마지막 레벨의 노드 수가 압도적이므로 Big-O에서 나머지는 무시

    3. 슬라이싱 비용 제거
       - candidates[i:]로 슬라이싱하면 매 노드마다 O(N) 복사 비용 발생
       - start 인덱스 방식으로 변경하여 이 비용을 O(1)로 줄임
       - 변경 전: O(N^(T/M) * N) = O(N^(T/M + 1))
       - 변경 후: O(N^(T/M))

SC: O((T/M) * N^(T/M))
    - 콜스택(call stack)의 최대 깊이 = T/M
    - 콜스택: 재귀 호출 시 각 함수의 변수(start, path, path_sum)가
      메모리에 쌓이는 공간. return하면 빠짐.
    - 동시에 쌓여있는 최대 프레임 수 = 재귀의 최대 깊이 = T/M
    - 예: candidates=[2,3,6,7], target=7 → 최대 4프레임 동시 존재
    - answer(결과 리스트): 최대 N^(T/M)개 조합 × 각 길이 T/M = O((T/M) * N^(T/M))
    - 콜스택 O(T/M)은 answer 공간에 비해 무시 가능하므로 전체 SC는 O((T/M) * N^(T/M))

풀이:
백트래킹으로 모든 조합을 탐색하되, 중복 조합 방지를 위해
start 인덱스를 활용하여 이전 후보는 건너뛰고, 같은 후보는 재사용 허용.
path_sum > target이면 가지치기(pruning)하여 불필요한 탐색을 줄임.
"""

from typing import *
import sys

input = sys.stdin.readline


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(start, path, path_sum):
            if path_sum > target:
                return

            if path_sum == target:
                answer.append(path[:])
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                path.append(candidate)
                path_sum += candidate
                backtrack(i, path, path_sum)
                path_sum -= candidate
                path.pop()

        backtrack(0, [], 0)

        return answer


candidates = list(map(int, input().split(",")))
target = int(input())
print(Solution().combinationSum(candidates, target))



"""
2,3,6,7
7
[[2,2,3],[7]]

2,3,5
8
[[2,2,2,2],[2,3,3],[3,5]]

2
1
[]
"""