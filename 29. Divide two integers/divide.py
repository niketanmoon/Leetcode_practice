class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        q = 0
        while d >= dv:
            temp = dv 
            mul = 1
            while d >= temp:
                # First take a difference
                d = d - temp
                # increase the quotient by 1
                q += mul

                # Now increase the divisor by 2
                temp = temp * 2
                mul += mul
        if (dividend < 0 and divisor >= 0) or (divisor <0 and dividend >= 0):
            q = - q
        if result > (2**31 - 1):
            return 2**31 -1
        elif result < (-2**31):
            return -2**31
        else:
            return result

