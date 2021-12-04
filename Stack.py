class Stack:
    def __init__(self, maxlen):
        self.stack = [None] * maxlen
        self.count = 0

    def push(self, item):
        if self.stack.__len__() == self.count:
            raise NotImplementedError

        self.stack[self.count] = item
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise ValueError

        self.count -= 1
        return self.stack[self.count]

    def peek(self):
        if self.count == 0:
            raise ValueError

        return self.stack[self.count - 1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def toString(self) -> str:
        content = self.stack
        return ''.join(content)


if __name__ == "__main__":
    stack = Stack(maxlen=10)
    for val in range(1, 10+1):
        stack.push(val)

    print(stack.peek())