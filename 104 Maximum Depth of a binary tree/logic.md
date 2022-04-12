- **Recursive DFS**
- If there is no root node return 0
- 1 is for root node + max(left subtree, right subtree)

- **BFS SOlution**
- First if there is no root node return 0
- Initialize the level to 0
- Now if there is a root node put it in a Queue 
- Now loop through the queue until its empty
- Now while looping, pop from the left and append the children back to the queue
- Once appending the children is done for loop is over and we can increase the level by 1

**Iterative DFS (Preorder traversal in a stack)**
- First if there is no root return 0
- Now initialise the stack with root and its depth
- Initialise the res = 0
- Now while stack is not empty
- pop from the stack node and its depth
- if node is there then first update the res as max depth and append the children 
- While updating the children, increment the depth
- return res