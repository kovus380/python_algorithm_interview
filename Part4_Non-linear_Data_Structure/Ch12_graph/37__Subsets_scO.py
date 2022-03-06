# 78 | Subsets
# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev_elements = []
        def dfs(depth, cnt, elements):
            if depth == cnt:
                res.append(prev_elements[:])
                return
            for elem in elements:
                next_elements = elements[elements.index(elem):]
                prev_elements.append(elem)

                next_elements.remove(elem)
                dfs(depth + 1, cnt, next_elements)
                prev_elements.pop()

        for i in range(len(nums) + 1):
            dfs(0, i, nums)
        return res


nums = [0]
sol = Solution()
res = sol.subsets(nums)
print(res)