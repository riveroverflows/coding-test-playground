from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                last = stack.pop()
                answer[last[1]] = i - last[1]
            stack.append([temperatures[i], i])
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(s.dailyTemperatures([30, 40, 50, 60]))
    print(s.dailyTemperatures([30, 60, 90]))
