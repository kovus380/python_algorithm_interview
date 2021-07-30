# 리스트로 변환


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            # isalunum() - check alphabet or numeric
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
            
        return True