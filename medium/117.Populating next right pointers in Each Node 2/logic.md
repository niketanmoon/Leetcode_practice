- If not root (Tree is empty) return None
- Now make the current as root
- Now while current is not empty
- First store the current in temp and assign current and currentNext pointers as None
- While temp is not null in this case current
**LEfT**
- Go to the left tree and link the next node
- When we go to left subtree, if it is for first time (check using currentNext is none or not)
- Make the current node to be the node at the left subtree
- And also the currentNext as the left subtree node
**RIGHT**
- Go to the right subtree and now current Next will not be null because we already know the previous Node
- Now link the currentNext.next to the right subtree node
- Now go through the level with temp = temp.next
