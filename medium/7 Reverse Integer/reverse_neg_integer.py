class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = - 1 * x
        original_number = x 
        reverse_number = 0
        while x > 0:
            last_digit = x % 10
            reverse_number = reverse_number * 10 + last_digit
            x = x // 10
        if reverse_number < -2**31 or reverse_number > 2**31 - 1:
            return 0
        if neg:
            return -1 * reverse_number
        return reverse_number