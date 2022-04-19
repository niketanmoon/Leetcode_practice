# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previousNode = dummy
        currentNode = head
        while currentNode:
        	if currentNode.val == val:
        		previousNode.next = currentNode.next
        	else:
        		previousNode = currentNode
        	currentNode = currentNode.next
       	return dummy.next