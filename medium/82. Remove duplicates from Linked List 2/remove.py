# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        first_node = head
        previousNode = dummy
        duplicate = False
        while first_node:
            second_node = first_node.next
            while second_node and second_node.val == first_node.val:
                duplicate = True
                second_node = second_node.next
            if not duplicate:
                previousNode = previousNode.next
            else:
                previousNode.next = second_node
                duplicate = False
            first_node = second_node
        return dummy.next