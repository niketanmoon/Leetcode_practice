- First check the base case if not node return None
- Now initialize a hashmap for all graph problems
- Now make a helper function which takes node
- If node is already in hashmap we dont need to create any node we can just return the copied node
- If node is not in hashmap we create a new node
- Now we go through each neighbor of the old node and call helper function to create copy of the node in the hashmap
- Also whatever neighbor node is returned by the function call to neighbors will be added to the copy node neighbors
- return copy node at last
- After the function is over just return dfs(node) 