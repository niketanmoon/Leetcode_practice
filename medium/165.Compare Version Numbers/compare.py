class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = list(map(int, version1.split(".")))
        list2 = list(map(int, version2.split(".")))
        s1 = 0
        s2 = 0
        len1 = len(list1)
        len2 = len(list2)
        while (s1 < len1) and (s2<len2):
            val1 = list1[s1]
            val2 = list2[s2]
            s1 += 1
            s2 += 1
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            else:
                continue
        
        while s1 < len1:
            val1 = list1[s1]
            s1 += 1
            if val1 > 0:
                return 1
        while s2 < len2:
            val2 = list2[s2]
            s2 += 1
            if val2 > 0:
                return -1
        
        return 0