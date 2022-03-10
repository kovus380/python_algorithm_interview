# 771 | Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 리스트 컴프리헨션을 이용하여 풀이
        answer = [stone for stone in stones if stone in jewels]
        return  len(answer)