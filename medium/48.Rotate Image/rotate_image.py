class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                
                # save top left
                topLeft = matrix[top][left + i]
                
                # replace top left with bottom left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # replace bottom left with bottom right
                matrix[bottom - i][left] = matrix[bottom][right-i]
                
                # replace bottom right with top right
                matrix[bottom][right-i] = matrix[top+i][right]
                
                # replace top right with top left
                matrix[top+i][right] = topLeft
            right -= 1
            left += 1