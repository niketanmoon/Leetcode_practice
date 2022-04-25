class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                mult = int(num1[i1]) * int(num2[i2])
                result[i1+i2] += mult 
                result[i1+i2+1] += result[i1+i2] // 10
                result[i1+i2] = result[i1+i2] % 10
        result, beg = result[::-1], 0
        while beg < len(result) and result[beg] == 0:
            beg += 1
        result = map(str, result[beg:])
        return "".join(result)