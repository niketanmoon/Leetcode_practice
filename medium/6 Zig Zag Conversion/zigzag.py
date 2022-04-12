class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        res = ""
        for row_number in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row_number, len(s), increment):
                res += s[i]
                if row_number > 0 and row_number < numRows -1 \
                and i + increment - 2*row_number < len(s):
                res += s[i + increment - 2*row_number]
        return res