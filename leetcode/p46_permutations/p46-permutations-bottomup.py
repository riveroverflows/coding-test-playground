nums = list(map(int, input().split(',')))
numslen = len(nums)

answer = []
used = set()
def backtrack(curr):
	if len(curr) == numslen:
		answer.append(curr[:])
		return

	for num in nums:
		if num in used:
			continue
		curr.append(num)
		used.add(num)
		backtrack(curr)
		used.remove(num)
		curr.pop()

backtrack([])
print(answer)