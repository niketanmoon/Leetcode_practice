class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def helper(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        helper(0, len(nums)-1)
        # reverse the first k half
        helper(0, k-1)
        # reverse the second k half
        helper(k, len(nums)-1)

        # first logic SC - O(n)
        # result = [0] * len(nums)
        # for i, num in enumerate(nums):
        #     result[(i+k)%len(nums)] = num

        # for i, num in enumerate(result):
        #     nums[i] = num