# 46 | Permulations
# https://leetcode.com/problems/permutations/
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))