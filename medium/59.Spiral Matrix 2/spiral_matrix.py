class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        count = 1
        while left < right and top < bottom:
            # iterate through top row
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            top += 1
            # iterate through right column
            for i in range(top, bottom):
                matrix[i][right-1] = count
                count += 1
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
            # iterate through bottom row
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = count
                count+=1
            bottom -=1
            
            # iterate through left column
            for i in range(bottom-1, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
        return matrix