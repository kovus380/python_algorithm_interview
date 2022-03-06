# 39 | Combination Sum
# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(csum, index, path):
            # Termination condition
            # csum value is exceeded target vaule
            if csum < 0:
                return
            # target value and csum match
            if csum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        dfs(target, 0, [])
        return result

candidates = [1, 2, 3]
target = 6
sol = Solution()
res = sol.combinationSum(candidates, target)
print(res)