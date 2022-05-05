# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = list()
        def dfs(node, currentSum, current):
            if not node:
                return
            current.append(node.val)
            currentSum += node.val
            if currentSum == targetSum and not node.left and not node.right:
                result.append(current)
                return
            dfs(node.left, currentSum, current.copy())
            dfs(node.right, currentSum, current.copy())
        dfs(root, 0, [])