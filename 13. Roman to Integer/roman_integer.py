class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        temp = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in reversed(s):
            if roman_dict[i] >= temp:
                result = result + roman_dict[i]
            else:
                result = result - roman_dict[i]
            temp = roman_dict[i]
        return result