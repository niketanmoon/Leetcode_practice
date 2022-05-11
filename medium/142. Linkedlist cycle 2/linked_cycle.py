# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # initialize fast = head
        fast = head
        
        # check if slow = fast 
        if fast == slow:
            return fast
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                break
        return fast