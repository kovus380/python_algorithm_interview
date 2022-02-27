# 39 | Combination Sum
# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        prev_elements = []
        def dfs(cnt, elements):
            if len(prev_elements) == cnt:
                if sum(prev_elements) == target:
                    results.append(prev_elements[:])
                return
            for cand in elements:
                prev_elements.append(cand)
                dfs(cnt, candidates[candidates.index(cand):])
                prev_elements.pop()
        for cnt in range(1, target // min(candidates) + 1):
            dfs(cnt, candidates)

        return results

candidates = [1]
target = 2
sol = Solution()
res = sol.combinationSum(candidates, target)
print(res)