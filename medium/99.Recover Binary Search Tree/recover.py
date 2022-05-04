# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.one = None
        self.two = None
        def inorder(current):
            if not current:
                return
            inorder(current.left)
            if self.prev and self.prev.val > current.val:
                # if first violation is not found yet then we take the first item which is current
                if not self.one:
                    self.one = self.prev
                # second violation update two to current
                self.two = current
            self.prev = current
            inorder(current.right)
        inorder(root)
        self.one.val, self.two.val = self.two.val, self.one.val