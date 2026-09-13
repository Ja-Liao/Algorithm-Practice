class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> int:
        for i in range(len(self.stack), 1, -1):
            self.stack2.append(self.stack.pop())
        num = self.stack.pop()
        self.stack = self.stack2[::-1]
        self.stack2 = []
        return num

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()