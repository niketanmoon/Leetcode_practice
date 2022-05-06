"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.current = root

        def linkNextNode(node):
            if not node:
                return

            if not self.currentNext:
                self.current = node
            else:
                self.currentNext.next = node
            self.currentNext = node


        while self.current:
            temp = self.curren
            self.current, self.currentNext = None, None
            while temp:
                linkNextNode(temp.left)
                linkNextNode(temp.right)
                temp = temp.next
        return root
