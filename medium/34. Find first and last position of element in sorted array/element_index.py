class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIdx = self.helper(nums, target, True)
        rightIdx = self.helper(nums, target, False)
        return [leftIdx, rightIdx]
    
    def helper(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right:
            middle = left + (right - left) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                i = middle
                if leftBias:
                    right = middle - 1
                else:
                    left = middle + 1