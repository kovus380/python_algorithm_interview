# 34 | Permulations
# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        stack = []
        answer = []
        for num in nums:
            need_visited = nums
            visited = nums
            del need_visited[need_visited.index(num)]
            print(need_visited)
            while need_visited:
                v = visited.pop()



nums = [1, 2, 3]
sol = Solution()
res = sol.permute(nums)
print(res)