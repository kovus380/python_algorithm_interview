# 77 | Combinations
# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        prev_elements = []
        nums = [num for num in range(1, n + 1)]
        def dfs(elements):
            if len(prev_elements) == k:
                result.append(prev_elements[:])
                return
            for e in elements:
                next_elements = elements[elements.index(e):]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

n = 4
k = 2
sol = Solution()
res = sol.combine(n, k)
print(res)
