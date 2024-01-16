from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def backtrack(start, curr):
            if len(curr) == k:
                results.append(curr[:])
                return

            for i in range(start, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.combine(n=4, k=2))
