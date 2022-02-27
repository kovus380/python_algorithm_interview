# 34 | Permulations
# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # append to results when leaf node (have no child node)
            if len(elements) == 0:
                results.append(prev_elements[:])

            # call recursive func for permutation generation
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


nums = [1, 2, 3]
sol = Solution()
res = sol.permute(nums)
print(res)