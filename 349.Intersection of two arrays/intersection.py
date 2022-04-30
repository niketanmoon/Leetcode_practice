class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique = set()
        result = list()
        for num in nums1:
            unique.add(num)
        
        for num in nums2:
            if num in unique:
                if num not in result:
                    result.append(num)
        return result