class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lcp = ""
        min_len = min([len(i) for i in strs])

        i = 0
        while i < min_len:
            # comparing each character of first string with the rest of the elements in an array
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return lcp

            # Wait for all the elements are matched and then add the char to the lcp
            lcp = lcp + char
            i = i + 1
        return lcp
