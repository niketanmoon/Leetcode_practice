# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        result = 0
        while q:
            qlen = len(q)
            levelSum = 0
            for i in range(qlen):
                node = q.popleft()
                if node:
                    levelSum += node.val
                    q.append(node.left)
                    q.append(node.right)
            if levelSum:
                result = levelSum
        return result