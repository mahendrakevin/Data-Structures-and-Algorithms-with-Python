class PriorityQueue:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.count = 0

    def add(self, item):
        if self.isFull():
            raise ValueError

        i = self.ShiftItemToInsert(item)
        self.items[i] = item
        self.count += 1

    def ShiftItemToInsert(self, item):
        idx = self.count - 1
        for i in range(idx, -1, -1):
            if self.items[i] > item:
                self.items[i + 1] = self.items[i]
            else:
                break
            idx -= 1
        return idx + 1

    def remove(self):
        if self.isEmpty():
            raise ValueError

        self.count -= 1
        return self.items[self.count]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self):
        return self.count == len(self.items)

    def toList(self):
        return self.items


if __name__ == "__main__":
    priorityqueue = PriorityQueue(capacity=5)
    priorityqueue.add(10)
    priorityqueue.add(5)
    priorityqueue.add(20)
    priorityqueue.add(1)
    priorityqueue.add(3)

    print(priorityqueue.toList())

    while not priorityqueue.isEmpty():
        print(priorityqueue.remove())