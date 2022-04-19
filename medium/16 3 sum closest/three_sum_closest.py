class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                current_sum = nums[i] + nums[s] + nums[e]
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
                if current_sum < target:
                    s += 1
                else:
                    e -= 1
        return res