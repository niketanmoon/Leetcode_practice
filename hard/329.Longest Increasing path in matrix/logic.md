- Go through each cell and apply dfs on each cell
- for dfs
- if you are out of the matrix or the cell value is less than the previous value then just return 0
- if the cell is already in dp that means visited we just return the path calculated
- otherwise we will calculate going up down right left as max(res, 1 + dfs(r+1, c, matrix[r][c])) 
- you can change rows and columns accordingly
- later once the result is updated as the max you just store it in the dp
- later we return it
- Now just go through each row and column in grid and call dfs(r, c, -1(which is the previousVal))
- return max(dp.values())