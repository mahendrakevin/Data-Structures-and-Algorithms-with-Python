from Stack import Stack


class MinStack:
    def __init__(self, maxlen):
        self.stack = Stack(maxlen)
        self.minStack = Stack(maxlen)

    def push(self, item: int):
        self.stack.push(item)

        if self.minStack.isEmpty():
            self.minStack.push(item)
        elif item < self.minStack.peek():
            self.minStack.push(item)

    def pop(self):
        if self.stack.isEmpty():
            raise ValueError

        top = self.stack.pop()

        if self.minStack.peek() == top:
            self.minStack.pop()

        return top

    def min(self):
        return self.minStack.peek()


if __name__ == "__main__":
    minStack = MinStack(3)
    minStack.push(40)
    minStack.push(20)
    minStack.push(30)
    print(minStack.minStack.stack)

