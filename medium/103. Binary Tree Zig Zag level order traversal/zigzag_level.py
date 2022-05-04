# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        q = collections.deque()
        q.append(root)
        reverse = False
        while q:
            level = list()
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if reverse:
                if level:
                    result.append(level[::-1])
            else:
                if level:
                    result.append(level)
            reverse = not reverse
        return result