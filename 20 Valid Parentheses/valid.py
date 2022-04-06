class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        brackets_mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for i in s:
            if i in brackets_mapping:
                stack.append(i)
            else:
                if not stack:
                    return False
                popped_char = stack.pop()
                if i != brackets_mapping[popped_char]:
                    return False
        return not stack