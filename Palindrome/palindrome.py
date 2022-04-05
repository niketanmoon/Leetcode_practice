class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if the number x is negative
        if x < 0:
        	return False
        original_number = x
        reverse_number = 0
        while x > 0:
        	last_digit = x % 10
        	reverse_number = reverse_number * 10 + last_digit
        	x = x // 10
        return original_number == reverse_number