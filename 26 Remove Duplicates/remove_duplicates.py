class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target_index = 1
        for idx in range(1, len(nums)):
        	previous_element = nums[idx-1]
        	current_element = nums[i]
        	if previous_element != current_element:
        		nums[target_index] = current_element
        		target_index += 1
        return target_index
