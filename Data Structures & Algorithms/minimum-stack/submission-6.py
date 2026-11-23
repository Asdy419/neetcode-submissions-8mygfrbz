class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.stack.append((val, self.mini))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.mini = float('inf')
            return
        else:
            self.mini = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
