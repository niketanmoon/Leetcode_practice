# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = list()
        if not root:
            return path
        self.dfs(root, "", path)
        return path
    
    def dfs(self, node, currentString, path):
        currentString += str(node.val)
        if not node.left and not node.right:
            path.append(currentString)
            return
        if node.left:
            self.dfs(node.left, currentString + "->", path)
        if node.right:
            self.dfs(node.right, currentString + "->", path)
