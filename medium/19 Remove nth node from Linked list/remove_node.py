# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previousNode, currentNode = dummy, head
        for i in range(n):
            if currentNode:
                currentNode = currentNode.next

        while currentNode:
            previousNode = previousNode.next
            currentNode = currentNode.next

        # delete
        previousNode.next = previousNode.next.next
        return dummy.next