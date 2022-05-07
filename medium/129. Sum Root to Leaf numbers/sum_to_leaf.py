# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, currentSum):
            if not node:
                return 0
            
            currentSum = currentSum * 10 + node.val
            # if it reaches leaf node
            if not node.left and not node.right:
                return currentSum
            
            return helper(node.left, currentSum) + helper(node.right, currentSum)
        
        return helper(root, 0)