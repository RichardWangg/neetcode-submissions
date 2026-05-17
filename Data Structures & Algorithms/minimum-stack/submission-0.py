class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.stack and self.minStack:
            self.minStack.append(min(self.getMin(), val))
        else:
            self.minStack.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack and self.minStack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        