# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.maxNodes = 0
        self.dfs(root)
        return self.maxNodes
    
    def dfs(self, root):
        if not root:
            return 
        # there is a node
        self.maxNodes += 1
        # go to left
        self.dfs(root.left)
        # go to right 
        self.dfs(root.right)