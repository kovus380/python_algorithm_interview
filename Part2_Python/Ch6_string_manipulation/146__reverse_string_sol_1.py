# 투 포인터를 이요한 스왑
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            # in one line, don't need to use temporary storage variable
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1