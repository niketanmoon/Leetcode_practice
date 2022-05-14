class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(numbers):
            secondNumber = target - num
            if secondNumber in hashmap:
                return [hashmap[secondNumber], idx+1]
            hashmap[num] = idx + 1
        return []