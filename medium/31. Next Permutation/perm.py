class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        # find pivot
        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                pivot = idx
                break
        if pivot == 0:
            nums.sort()
            return
        
        # swap the first element with the pivot
        swap = len(nums) - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
        
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])