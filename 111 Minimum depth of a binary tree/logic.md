-  Here first check if the root is empty then return 0
- Now iterate and make a recursive dfs 
- The depth will be calculated as 1 + min(fn(root.left), fn(root.right) )
- This has a edge case what if the binary tree is a skewed left tree or right tree
**Left Skewed Tree**
- If the tree is left skewed then min root.left, root.right will always return 0 since root.left = 1 and root.right =0
- Thus it will not add for the depth
**Right Skewed Tree**
- This is similar to left sub tree
- Now to tackle this we can check if the tree is left skewed or right skewed and whenever this is the case it should return
- 1 + fn(root.left) + fn(root.right)
- THis way if its left skewed then it will become root + left + 0 which is correct
- This also holds for right subtree