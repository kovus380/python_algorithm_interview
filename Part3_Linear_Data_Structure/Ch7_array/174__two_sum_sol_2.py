# 타켓에서 첫 번째 값을 뺀 값 target - n 이 존재하는지 탐색
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))