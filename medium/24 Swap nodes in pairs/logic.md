- Initialize dummy as previous node to head
- prev = dummy and current = head
- Now while currentNode current Node.next is not empty
- we change currentNode.next.next to currentNode
- Now change the currentNode.next link to currentNode.next.next
- Now we update the previous node.next to current node.next
- Update ptrs = previous node = currentNode and currentNode = currentNode.next.next