class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is an empty string
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)]:
                return i
        return -1