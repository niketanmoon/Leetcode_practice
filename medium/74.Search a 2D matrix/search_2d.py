class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        while top <= bottom:
            middleRow = top + (bottom-top)//2
            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottom = middleRow - 1
            else:
                break
        if not (top <= bottom):
            return False
        
        currentRow = top + (bottom - top) // 2
        left, right = 0, columns - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target > matrix[currentRow][middle]:
                left = middle + 1
            elif target < matrix[currentRow][middle]:
                right = middle - 1
            else:
                return True
        return False