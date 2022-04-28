# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tailNode = 1, head
        # get the length and shift tail to last node
        while tailNode.next:
            tailNode = tailNode.next
            length += 1
        
        # k = 6 length = 5 then k = 6 % 5 = 1
        k = k % length
        if k == 0:
            return head
        currentNode = head
        
        # going till the pivot
        for i in range(length - k - 1):
            currentNode = currentNode.next
        
        newHead = currentNode.next
        currentNode.next = None
        tailNode.next = head
        return newHead