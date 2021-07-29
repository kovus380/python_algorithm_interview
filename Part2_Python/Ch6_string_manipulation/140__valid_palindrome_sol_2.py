

import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs: Deque = collections.deque() # declare data type deque

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
