class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        checker = set("0123456789")
        neg = False

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # whitespace
        while i < len(s) and s[i] == " ":
            i += 1

        # +/- symbol
        if i < len(s) and s[i] == "-":
            neg = True
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1

        # If it is a number then add
        while i < len(s) and s[i] in checker:
            res = res * 10 + int(s[i])
            i += 1

        if neg:
            res = - res

        if res < 0:
            return max(res, MIN_INT)
        else:
            return min(res, MAX_INT)