# 딕셔너리 이용
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # exchange key and value and save as dictionary
        for i, num in enumerate(nums):
            nums_map[num] = i

        # provide case : nums = [3, 2, 4], target = 6
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


sol = Solution()
nums = [3, 3]
target = 6
print(sol.twoSum(nums, target))