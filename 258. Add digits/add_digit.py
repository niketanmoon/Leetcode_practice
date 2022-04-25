class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        def helper(currentNumber):
            currentResult = 0
            if len(str(currentNumber)) == 1:
                return currentNumber
            
            while currentNumber:
                last_digit = currentNumber % 10
                currentResult += last_digit
                currentNumber =  currentNumber // 10
                
            if len(str(currentResult)) != 1:  
                return helper(currentResult)
            else:
                return currentResult
        
        return helper(num)