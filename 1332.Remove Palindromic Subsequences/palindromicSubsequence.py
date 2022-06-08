class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = len(s) - 1
        if self.isPalindrome(s, left, right):
            return 1
        return 2
        
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True