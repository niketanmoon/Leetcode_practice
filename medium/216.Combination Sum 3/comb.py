class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        candidates = [i for i in range(1, 10)]
        
        def dfs(pos, current, target):
            if target == 0:
                if len(current) == k:
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
        dfs(0, [], n)
        return result