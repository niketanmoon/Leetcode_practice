#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.nums = list()
        while head:
            self.nums.append(head.val)
            head = head.next
        def helper(left, right):
            if left > right:
                return None
            mid = left + (right-left)//2
            root = TreeNode(self.nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        
        return helper(0, len(self.nums)-1)