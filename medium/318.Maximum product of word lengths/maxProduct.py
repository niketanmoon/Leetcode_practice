class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        state = [0] * n
        for i in range(n):
            for c in words[i]:
                state[i] |= 1 << (ord(c)-ord("a"))
                
        maxProduct = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (state[i] & state[j]):
                    maxProduct = max(maxProduct, len(words[i])*len(words[j]))
        return maxProduct