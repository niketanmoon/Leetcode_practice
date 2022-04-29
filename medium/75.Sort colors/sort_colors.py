# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # use bucket sort
#         hashmap = {}
#         for num in nums:
#             hashmap[num] = 1 + hashmap.get(num, 0)
#         idx = 0
#         for i in range(3):
#             if hashmap.get(i):
#                 for c in range(hashmap[i]):
#                     nums[idx] = i
#                     idx += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                # swap it with left and increment mid and left
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                # swap it with right and decrement only the right
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1