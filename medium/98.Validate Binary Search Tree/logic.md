- Define left and right boundaries for root it will be -inf to inf
- Now we first check if node does not have any left or right then return True
- Also check for false condition first
- if node value lies between left boundary and right boundary then its ok but if its not then return False
- if node value lies between left and right boundary then we call recursive function on left subtree with left boundary as it is and right boundary as the parent node value
- Similarly call recursive function on right subtree where the parent node value is the left boundary and right boundary is as it is.
- If both of these left subtree and right subtree returns True then only return True