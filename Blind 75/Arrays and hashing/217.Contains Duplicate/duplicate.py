class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TC - O(n^2) SC- O(1) 
        # TLE
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        # TC- O(n) SC- O(n)
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = True
        return False