class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        matrix = [[float("inf") for _ in range(COLS+1)] for _ in range(ROWS+1)]
        matrix[ROWS-1][COLS] = 0
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS-1, -1, -1):
                matrix[r][c] = grid[r][c] + min(matrix[r+1][c], matrix[r][c+1])
        return matrix[0][0]