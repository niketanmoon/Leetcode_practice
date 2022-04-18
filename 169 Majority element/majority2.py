class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 0
        for num in nums:
        	if result != num:
        		if count > 0:
        			count -= 1
        		else:
        			result = num
        			count += 1
        	else:
        		count += 1
        return result