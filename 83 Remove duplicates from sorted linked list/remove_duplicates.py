class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_node = head
        while first_node:
            second_node = first_node.next
            while second_node and second_node.val == first_node.val:
                second_node = second_node.next
            first_node.next = second_node
            first_node = second_node
        return head