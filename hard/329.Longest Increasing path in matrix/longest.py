class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r, c, previousVal):
            # out of bounds case
            if (r<0 or r == rows or 
               c < 0 or c == cols or
               matrix[r][c] <= previousVal):
                return 0
            
            # repeated work check
            if (r, c) in dp:
                return dp[(r, c)]
            result = 1
            result = max(result, 1+dfs(r+1,c, matrix[r][c]))
            result = max(result, 1+dfs(r-1,c, matrix[r][c]))
            result = max(result, 1+dfs(r,c+1, matrix[r][c]))
            result = max(result, 1+dfs(r,c-1, matrix[r][c]))
            dp[(r, c)] = result
            return result
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        return max(dp.values())