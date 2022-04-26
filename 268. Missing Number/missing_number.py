class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += i - nums[i]
        return result

        # Using xor
        result = len(nums)
        for i in range(len(nums)):
            result = result ^ i ^ nums[i]
        return result