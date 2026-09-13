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
        for i in range(len(self.stack), 1, -1):
            self.stack2.append(self.stack.pop())
        num = self.stack[-1]
        while self.stack2:
            self.stack.append(self.stack2.pop())
        # self.stack = num + self.stack2[::-1]
        # self.stack2 = []
        return num

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()