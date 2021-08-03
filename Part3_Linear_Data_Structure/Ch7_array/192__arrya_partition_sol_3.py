# 파이썬 다운 방식
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

sol = Solution()
nums = [6,2,6,5,1,2]
print(sol.arrayPairSum(nums))