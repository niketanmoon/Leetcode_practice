class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            middleNumber = nums[middle]
            leftNumber = nums[left]
            rightNumber = nums[right]

            # First go in the left sorted array
            if leftNumber <= middleNumber:

                # Now define conditions to go to right
                if target > middleNumber or target < leftNumber:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                # right portion
                # define condition for going left
                if target < middleNumber or target > rightNumber:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1