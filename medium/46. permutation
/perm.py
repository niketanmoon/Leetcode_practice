class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            #remove from the first position
            n = nums.pop(0)
            # Now make a recurcive call
            perms = self.permute(nums)
            
            # Now add the popped value to the permutations
            for perm in perms:
                perm.append(n)
            
            # Add both the list to the result - use extend
            result.extend(perms)
            
            # add back the removed num
            nums.append(n)
        return result