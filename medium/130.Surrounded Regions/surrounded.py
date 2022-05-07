class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def helper(r, c):
            # Check for base case 
            if (r<0 or c<0 or r==rows or c==cols or board[r][c] != "O"):
                return
            board[r][c] = "T"
            helper(r-1, c)
            helper(r+1, c)
            helper(r, c-1)
            helper(r, c+1)
        
        # change unsurrounded O to T
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1])):
                    helper(r, c)
        
        # change all "O" to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # change "T" to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"