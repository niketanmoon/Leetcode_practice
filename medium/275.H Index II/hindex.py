class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        left, right = 0, l - 1
        total = 0
        while left <= right:
            middle = left + (right-left) // 2
            if citations[middle] >= l - middle:
                total = max(total, l-middle)
                right = middle - 1
            else:
                left = middle + 1
        return total