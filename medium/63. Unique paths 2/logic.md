- First define the row and column and initialize a matrix of 0s
- Make the first row of all 1 except for obstaclegrid which has 1
- Now first row go through the columns and wherever there is obstacle grid == 1  just break else put 1 
- Now go through each row first column and wherever there is obstacle grid == 1 just break else put 1 else where
- Now go from second row and second column and if the obstaclegrid for that row is 1 then put matrix box = 0
- else matrix[r][c] = matrix[r-1][c] + matrix[r][c-1 ] which is up + left
- return matrix[-1][-1]