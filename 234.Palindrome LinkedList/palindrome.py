# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        # reach middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse
        previousNode = None
        while slow:
            temp = slow.next
            slow.next = previousNode
            previousNode = slow
            slow = temp 

        left, right = head, previousNode
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

