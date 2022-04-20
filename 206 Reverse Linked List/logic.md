**Iterative method using two pointers**
- Create two pointers
- previous pointer will point to null and next pointer is head
- Before breaking a link of current.next and linking it to null first store the second node in temp
- Now currentnode.next = previous
- then increment both the nodes
- prev = current
- current = temp.next
- return previous