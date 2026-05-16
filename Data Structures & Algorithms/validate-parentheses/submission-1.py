class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        openers = {'(': ')', '{': '}', '[': ']'}
        closers = {')', '}', ']'}

        for c in s:
            if c in openers:
                stack.append(c)
                continue
            if not stack or c != openers[stack.pop()]:
                return False
        
        return len(stack) == 0