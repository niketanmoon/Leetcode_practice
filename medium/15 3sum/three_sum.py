class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx-1] == num:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                target_sum = val + nums[left] + nums[right]
                if target_sum > 0:
                    right -= 1
                elif target_sum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            return res