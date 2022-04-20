# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previousNode, currentNode = dummy, head
        while currentNode and currentNode.next:
            nxtPair = currentNode.next.next
            second = currentNode.next
            
            second.next = currentNode
            currentNode.next = nxtPair
            previousNode.next = second
        
            previousNode = currentNode
            currentNode = nxtPair
        return dummy.next