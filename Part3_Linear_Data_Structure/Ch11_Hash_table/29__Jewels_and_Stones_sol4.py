# 771 | Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)