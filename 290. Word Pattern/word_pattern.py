class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        mapCW = {}
        mapWC = {}
        for c, w in zip(pattern, words):
            if c in mapCW and mapCW[c] != w:
                return False
            if w in mapWC and mapWC[w] != c:
                return False
            mapCW[c] = w
            mapWC[w] = c
        return True