class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        myList = list()
        i = 0
        while i < len(nums):
            while (i+1 < len(nums)) and (nums[i+1] == nums[i] + 1):
                i += 1
            if start != nums[i]:
                myList.append(f"{start}->{nums[i]}")
            else:
                myList.append(str(start))
            i += 1
        return myList