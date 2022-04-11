class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        b = 0
        hash_set = set()
        ls = 0
        while b < len(s):
            if s[b] not in hash_set:
                hash_set.add(s[b])
                b += 1
                ls = max(ls, len(hash_set))
            else:
                hash_set.remove(s[a])
                a += 1
        return ls