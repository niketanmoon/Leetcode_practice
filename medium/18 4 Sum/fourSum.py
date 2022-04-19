class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def helper(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i >start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    helper(k-1, i + 1, target - nums[i])
                    quad.pop()
                return
            left, right = start, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        helper(4, 0, target)
        return res