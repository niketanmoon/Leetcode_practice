class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitsToCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            for c in digitsToCharMap[digits[i]]:
                backtrack(i+1, currentString+c)
        
        if digits:
            backtrack(0, "")