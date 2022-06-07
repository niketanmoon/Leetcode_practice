class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque
        
        edgs = {i:set() for i in range(n)}
        for u,v in edges: edgs[u].add(v); edgs[v].add(u)
        dq=deque([i for i in range(n) if len(edgs[i])==1])
        
        nodes=n
        while nodes>2:
            new=set()
            for i in range(len(dq)):
                temp=dq.popleft()
                for pos in edgs[temp]:
                    if pos in new: continue
                    edgs[pos].remove(temp)
                    if len(edgs[pos])==1: dq += [pos]; new.add(pos)
                edgs.pop(temp)
                nodes-=1
                
        if not edges: return [0]
        return list(dq)