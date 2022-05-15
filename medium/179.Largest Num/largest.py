class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # first convert all numbers into string
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1+n2 > n2+n1:
                # if we have to return n1 + n2
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))