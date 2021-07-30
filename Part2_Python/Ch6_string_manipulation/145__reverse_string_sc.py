# 244 | Reverse String
# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp


sol = Solution()
s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)