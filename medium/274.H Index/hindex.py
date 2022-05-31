class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        bucket = [0] * (l+1)
        sum = 0
        for num in citations:
            if num >= l:
                bucket[l] += 1
            else:
                bucket[num] += 1
        i = l
        while i >= 0:
            sum += bucket[i]
            if sum >= i:
                return i
            i -= 1
        return 0