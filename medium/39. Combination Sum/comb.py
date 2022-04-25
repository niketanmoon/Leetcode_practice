class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # First add candidate to the list
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            
            # Dont add the candidate to the list
            current.pop()
            dfs(i + 1, current, total)
        dfs(0, [], 0)
        return result