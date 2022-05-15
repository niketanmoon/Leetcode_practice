- Apply iterative BFS
- First initialize the stack
- Now while there is a node add all the left nodes to the stack
**hasNext**
- return if stack is empty or not
**next**
- First it will pop the node
- Then it will first check if it has a right node
- If it has a right node then it will add the right node and all its left node
- then return the pop node value