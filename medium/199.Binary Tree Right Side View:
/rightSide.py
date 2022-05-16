# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = list()
            # rightNode = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # rightNode = node 
                    q.append(node.left)
                    q.append(node.right)
            #if rightNode:
            # result.append(rightNode.val)
            if level:
                result.append(level[-1])
        return result