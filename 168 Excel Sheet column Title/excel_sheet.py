class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            c = chr(ord('A') + (columnNumber - 1) % 26)
            res = c + res
            columnNumber = (columnNumber - 1) // 26
        return res