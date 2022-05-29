class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, count1, count2 = 0, 0, 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        output = list()
        freq1 = freq2 = 0
        for num in nums:
            if candidate1 == num:
                freq1 += 1
            elif candidate2 == num:
                freq2 += 1
        if freq1 > len(nums) // 3:
            output.append(candidate1)
        if freq2 > len(nums) // 3:
            output.append(candidate2)
        return output