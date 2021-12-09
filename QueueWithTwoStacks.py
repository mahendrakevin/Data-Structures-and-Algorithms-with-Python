class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError

        self.MoveStack1ToStack2()

        return self.stack2.pop()

    def MoveStack1ToStack2(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def peek(self):
        if self.isEmpty():
            raise ValueError

        self.MoveStack1ToStack2()

        return self.stack2[-1]

    def isEmpty(self) -> bool:
        return self.stack1 is [] and self.stack2 is []

    def toList(self):
        return self.stack2

if __name__ == "__main__":
    queuestack = QueueWithTwoStacks()
    queuestack.enqueue(10)
    queuestack.enqueue(20)
    queuestack.enqueue(30)
    item = queuestack.dequeue()
    print(item)
    print(queuestack.toList())