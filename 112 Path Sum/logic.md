- Make a helper function and pass it a node and current sum
- Now check if node is None then return False
- Now update the current sum
- We have to check if we reached the leaf node
- If its a leaf node we will return current_sum == targetsum
- Else we will go to left subtree and see if the target sum matches 
- Or we can also go to the right subtree and do the same 
- If any one of them returns True then we return True