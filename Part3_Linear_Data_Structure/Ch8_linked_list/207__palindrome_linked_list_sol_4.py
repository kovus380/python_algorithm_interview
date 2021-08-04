# Using Runner
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # using runner, implement reverse linked list
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # if the number of input values is odd - pass
        if fast:
            slow = slow.next

        # check Palindrome
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev