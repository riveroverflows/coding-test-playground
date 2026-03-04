# import itertools

# n = int(input())
# k = int(input())
# set_ = []
# for i in range(1, n + 1):
#     set_.append(i)

# seq = list(itertools.permutations(set_))
# print("".join(list(map(str, seq[k - 1]))))

# =================

# from typing import *

# class Permutation:

#     def permute(self, input_number: int) -> List[List[int]]:
#         permutations = []
#         used = set()

#         nums = []
#         for i in range(1, input_number + 1):
#             nums.append(i)

#         self._permute(permutations, used, nums, input_number, [])
#         return permutations

#     def _permute(self, permutations, used, nums, target_number: int, curr: List[int]):
#         if len(curr) == target_number:
#             permutations.append(curr[:])
#             return

#         for num in nums:
#             if num in used:
#                 continue

#             curr.append(num)
#             used.add(num)

#             self._permute(permutations, used, nums, target_number, curr)

#             used.remove(num)
#             curr.pop()


# n = int(input())
# k = int(input())

# permutations = Permutation().permute(n)
# for i, p in enumerate(permutations):
#     print(f"{i+1}:, {p}")
# print("".join(map(str, permutations[k - 1])))


# ============


# 1,2,3,4 로 만들어진 순열의 9번째를 찾아야하는데...
# 맨 첫자리 숫자는 첫번째 자리를 1개를 제외한 나머지 숫자 개수의 factorial만큼 반복됨
# 여기서는 1이 첫번째 자리에 오면 나머지 2,3,4로 순열을 만드는거니까 1로 시작하는 순열은 6번째까지가 되는거임
# 전체 순열 중 9번째를 찾아야되는데 위에 방식대로 계산해보면
# 첫번째 자리는 2가됨.
# 그다음 숫자는 2를 제외하고 1,3,4 중에서 찾아야함. 이미 9번째 중에서 6번째만큼왔으니까 1,3,4로 만들어지는 순열중에서 3번째를 찾아야함.
# 1로 고정하면 나머지 숫자 두개로 만들수 있는 경우가 2! = 2니까 두번째 자리에 1이 아니게됨
# 같은 방식으로 계산해서 세번째 자리를 3으로 확정할 수 있음.
# 이제 9-6-2 까지 했으니 다음 숫자는 바로 1로 확정할 수 있음.
# 이제 자연스럽게 2314로 확정할 수 있음.

# 근데 이걸 어떻게 알고리즘으로 풀어내지?
# 

from math import factorial

n = int(input())
k = int(input())

answer = ""

used = [-1] * n

remain = k%factorial(n-1)

