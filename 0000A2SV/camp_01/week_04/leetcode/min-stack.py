class MinStack:

    def __init__(self):
        self.original_stack = []
        # monotonically decreasing stack
        self.min_stack = []

    def push(self, val: int) -> None:
        # if the stack is empty or 
        # if the new value is less than 
        # the one at the top append it 
        if len(self.min_stack) == 0  or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.original_stack.append(val)

    def pop(self) -> None:
        # pop only if the top elements are equal
        if self.original_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.original_stack.pop()

    def top(self) -> int:
        return self.original_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()