answer = []
nums = list(map(int, input().split(',')))
num_len = len(nums)

arr = []
used = set()
def backtracking(nums):
	if len(arr) == num_len:
		answer.append(arr[:])
		return

	for num in nums:
		if num in used:
			continue
		arr.append(num)
		used.add(num)
		backtracking(nums)
		used.remove(num)
		arr.pop()

backtracking(nums)
print(answer)
"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

