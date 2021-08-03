from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

sol = Solution()
nums = [6,2,6,5,1,2]
print(sol.arrayPairSum(nums))