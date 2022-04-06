# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = list()
        while list1:
            merged_list.append(list1.val)
            list1 = list1.next
        while list2:
            merged_list.append(list2.val)
            list2 = list2.next

        merged_list.sort()
        s = ListNode()
        t = ListNode()
        for node_val in merged_list:
            s.next = ListNode(node_val)
            s = s.next
        return t.next