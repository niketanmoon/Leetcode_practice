- let prevnode = one node before head
- Now let current node = head
- Shift the current node by the position given in this case n
- Now keep incrementing current node and prev node untill current node is empty
- Once current node is empty we know that prev node.next is the node we want to remove
- prevNode.next = prevNode.next.next
- return dummy.next