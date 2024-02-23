class MyStack:

    def __init__(self):
        self.__stack = deque()
        
    def push(self, x: int) -> None:
        self.__stack.appendleft(x)

    def pop(self) -> int:
        return self.__stack.popleft()
        
    def top(self) -> int:
        return self.__stack[0]
        
    def empty(self) -> bool:
        return len(self.__stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()