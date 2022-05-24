class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list
        prereq = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
            
        # A course has 3 possible states
        # 1. Visited course has been added to output
        # 2. Visiting course not added to output but it is in cycle
        # 3. unvisited - course not added to output or cycle
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output