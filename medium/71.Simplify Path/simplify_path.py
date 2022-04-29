class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        current = ""
        for c in path + "/":
            if c == "/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current != "" and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += c
        return "/" + "/".join(stack)