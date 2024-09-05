class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c is ')' or c is '}' or c is ']':
                if not stack:
                    return False
                if c is ')':
                    if stack[-1] is '(':
                        stack.pop()
                    else:
                        return False
                if c is '}':
                    if stack[-1] is '{':
                        stack.pop()
                    else:
                        return False
                if c is ']':
                    if stack[-1] is '[':
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(c)
        return not stack