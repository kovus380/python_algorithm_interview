# 77 | Combinations
# https://leetcode.com/problems/combinations/
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

n = 4
k = 2
sol = Solution()
res = sol.combine(n, k)
print(res)
