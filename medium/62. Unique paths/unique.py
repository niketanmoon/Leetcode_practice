class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom row
        row = [1] * n

        # iterate through row except last
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-1, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]