class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        output = 0
        maxF = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxF = max(maxF, count[s[right]])
            while (right-left+1) - maxF > k:
                count[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output
#         count = {}
#         output = 0
#         l = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             while (r-l+1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1
#             output = max(output, r-l+1)
#         return output