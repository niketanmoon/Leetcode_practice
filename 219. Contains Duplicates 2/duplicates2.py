class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for idx, num in enumerate(nums):
            if num in hashMap and abs((idx - hashMap.get(num))) <= k:
                return True
            hashMap[num] = idx
        return False