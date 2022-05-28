class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = list()
        previousSymbol = "+"
        previousNumber = 0
        alpha = "+-/*"
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                previousNumber = previousNumber * 10 + int(c)
                
            if c in alpha or i == (len(s) - 1):
                if previousSymbol == "+":
                    stack.append(previousNumber)
                elif previousSymbol == "-":
                    stack.append(-previousNumber)
                elif previousSymbol == "/":
                    stack[-1] = int(stack[-1] / previousNumber)
                elif previousSymbol == "*":
                    stack[-1] *= previousNumber

                # reset
                previousNumber = 0
                previousSymbol = c
        return sum(stack)