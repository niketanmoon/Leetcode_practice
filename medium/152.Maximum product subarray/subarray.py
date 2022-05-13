class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currentMin, currentMax = 1, 1
        for num in nums:
            if num == 0:
                currentMin, currentMax = 1, 1
                continue
            a = num * currentMax
            b = num * currentMin
            currentMax = max(a, b, num)
            currentMin = min(a, b, num)
            result = max(result, currentMax)
        return result