class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        
        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            matrix[0][c] = 1
        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            matrix[r][0] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
        return matrix[-1][-1]