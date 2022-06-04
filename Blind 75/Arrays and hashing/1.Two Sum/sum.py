class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            secondNumber = target - num
            if secondNumber in hashMap:
                return [idx, hashMap[secondNumber]]
            hashMap[num] = idx
        return []