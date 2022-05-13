class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right-left)//2
            if nums[middle] < nums[middle+1]:
                left = middle + 1
            else:
                right = middle
        return left