class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for num in nums:
            # checking the left number is there or not
            if (num-1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                maxCount = max(length, maxCount)
        return maxCount