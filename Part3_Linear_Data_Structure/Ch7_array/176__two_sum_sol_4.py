# 앞선 sol3 개선 -> for 문 하나로
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

sol = Solution()
nums = [3, 3]
target = 6
print(sol.twoSum(nums, target))