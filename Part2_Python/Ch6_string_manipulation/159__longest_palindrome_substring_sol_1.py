# 5 | Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                print("=="*20, left, right, s[left + 1:right])
                left -= 1
                right += 1
            print("^^", left, right, s[left + 1:right])
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s)-1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
            print("%", i, result)
        return result

sol = Solution()
s = "abcdkkokk"
print(22, sol.longestPalindrome(s))