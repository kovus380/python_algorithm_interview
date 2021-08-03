# 561 | Array Partition I
# https://leetcode.com/problems/array-partition-i/
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0

        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum

sol = Solution()
nums = [6,2,6,5,1,2]
print(sol.arrayPairSum(nums))