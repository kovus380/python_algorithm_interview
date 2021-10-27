# 20 | Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        parenthneses = {'{': '}', '(': ')', '[': ']'}
        while s:
            stack.append(s.pop())
            while len(stack) >= 2 and stack[-1] in parenthneses and stack[-2] == parenthneses[stack[-1]]:
                stack.pop()
                stack.pop()
        return False if stack else True
