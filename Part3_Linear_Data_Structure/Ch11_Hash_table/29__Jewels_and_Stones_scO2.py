# 771 | Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # set에서의 in 연산효율성을 고려하여 set으로 변환해줌
        jewel = set(jewels)

        answer = [stone for stone in stones if stone in jewel]
        return len(answer)