class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndex = {}
        visited = set()
        stack = []
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and lastIndex[stack[-1]] > i):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)