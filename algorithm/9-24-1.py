class MyQueue:

    def __init__(self):
        self.front = []
    def push(self, x: int) -> None:
        self.front.append(x)
    def pop(self):
        if not self.front:
            return None
        else:
            return self.front.pop(0)

    def peek(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        if not self.front:
            return True
        else:
            return False

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.empty())
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
    print(queue.pop())
    print(queue.empty())


