class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentIdx = 0
        endIdx = 0
        startIdx = 0
        while endIdx < len(nums):
            while (endIdx < len(nums) and nums[endIdx] == nums[startIdx]):
                endIdx += 1
            numLength = endIdx - startIdx
            allowedLength = min(numLength, 2)
            for _ in range(allowedLength):
                nums[currentIdx] = nums[startIdx]
                currentIdx += 1
            startIdx = endIdx
        return currentIdx