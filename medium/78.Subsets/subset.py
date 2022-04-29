class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        subset = list()
        
        def backtrackDFS(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrackDFS(i+1)
            subset.pop()
            backtrackDFS(i+1)
        
        backtrackDFS(0)
        return result