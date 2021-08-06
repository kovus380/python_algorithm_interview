# 206 | Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 모르겠음
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        while head.next != None:
            head.next = head.next
            return head.next