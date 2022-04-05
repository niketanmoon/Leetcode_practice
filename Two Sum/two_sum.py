class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, num in enumerate(nums):
            second_number = target - num
            if second_number in hash_map:
                return [idx, hash_map[second_number]]
            hash_map[num] = idx 
        return []