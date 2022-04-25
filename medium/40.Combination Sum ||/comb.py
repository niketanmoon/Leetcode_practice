class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(pos, current, target):
            if target == 0:
                result.append(current.copy())
                return
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                dfs(i+1, current, target - candidates[i])
                current.pop()
                prev = candidates[i]
        dfs(0, [], target)
        return result