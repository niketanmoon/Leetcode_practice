- Take l = 0 and r = len(array) - 1
- we are going to search the middle element of the array and convert it to Tree Node
- Later we go to the left subtree and right subtree
- While going to left subtree, move the right to middle - 1 and for right subtree move the left to middle + 1
- Continue this untill left > right
- return root node