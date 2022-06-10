class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        hashSet = set()
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[r])
            result = max(result, r - left + 1)
        return result