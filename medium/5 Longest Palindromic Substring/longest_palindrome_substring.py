class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = ""
        for i in range(len(s)):
            l, r = i,i
            # check if the string is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(max_string):
                    max_string = s[l:r+1]
                l -= 1
                r += 1

            # for even string
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(max_string):
                    max_string = s[l:r + 1]
                l -= 1
                r += 1
        return max_string