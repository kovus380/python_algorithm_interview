

# 125 | Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        words = []
        for alpha in s:
            if alpha in [chr(i) for i in range(97, 123)] or alpha in [chr(j) for j in range(48, 58)]:
               words.append(alpha)
        tag = True
        for idx in range(len(words)//2):
            if words[idx] != words[len(words)-1-idx]:
                tag = False
        return tag

f = Solution()
f.isPalindrome("9,8")