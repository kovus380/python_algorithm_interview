# 15 | 3sum
# https://leetcode.com/problems/3sum/

# 시간 초과 난다
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    num_list = sorted([nums[i], nums[j] , nums[k]])
                    if sum(num_list) == 0 and num_list not in answers:
                        answers.append(num_list)
        return answers

sol = Solution()
nums = [0]
print(sol.threeSum(nums))