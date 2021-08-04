# 234 | Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Using List Conversion
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q: List = []

        if not head:
            return True

        node = head

        # List Conversion
        while node is not None:
            q.append(node.val)
            node = node.next

        # Check Palindrome
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


