import collections


class MyCircularQueue:

    def __init__(self, k: int):
        self.circle = []
        self.rear = 0
        self.front = 0
        self.circleLength = k
    def enQueue(self, value: int) -> bool:
        if self.circleLength == len(self.circle):
            return False
        else:
            self.circle.append(value)
            self.rear = len(self.circle)-1
            return True
    def deQueue(self) -> bool:
        if not self.circle:
            return False
        else:
            self.circle.pop(0)
            self.rear = len(self.circle) - 1
            return True
    def Front(self) -> int:
        if not self.circle:
            return -1
        else:
            return self.circle[self.front]
    def Rear(self) -> int:
        if not self.circle:
            return -1
        else:
            return self.circle[self.rear]
    def isEmpty(self) -> bool:
        return not self.circle
    def isFull(self) -> bool:
        if len(self.circle) == self.circleLength:
            return True
        else:
            return False

if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(10)

    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())
    print(myCircularQueue.isFull())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())


