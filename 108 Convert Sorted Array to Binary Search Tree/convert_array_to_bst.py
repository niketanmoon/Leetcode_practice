# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(left_index, right_index):
            if left_index > right_index:
                return None
            middle_index = left_index + (right_index - left_index) // 2
            root = TreeNode(nums[middle_index])
            root.left = helper(0, middle_index - 1)
            root.right = helper(middle_index + 1, right)
            return root
        return helper(0, len(nums) - 1)