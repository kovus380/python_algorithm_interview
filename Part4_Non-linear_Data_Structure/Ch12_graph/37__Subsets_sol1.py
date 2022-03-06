# 78 | Subsets
# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # add results every times
            result.append(path)

            # while making path, DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, "")
        return res


nums = [0]
sol = Solution()
res = sol.subsets(nums)
print(res)