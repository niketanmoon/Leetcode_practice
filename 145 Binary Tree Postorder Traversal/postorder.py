# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        def helper(node):
        	if not node:
        		return
        	
        	helper(node.left)
        	helper(node.right)
            result.append(node.val)
        helper(root)
        return result
                    