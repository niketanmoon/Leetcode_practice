class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC - O(n) SC - O(n)
        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for c in s:
            hashMapS[c] = 1 + hashMapS.get(c, 0)
        for c in t:
            hashMapT[c] = 1 + hashMapT.get(c, 0)
        
        for k in hashMapS:
            if k in hashMapT and (hashMapS[k] == hashMapT[k]):
                continue
            return False
        return True