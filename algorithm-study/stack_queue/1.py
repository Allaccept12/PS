class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack():
    def __init__(self):
        self.top = None

    def push(self,value):
        self.top = Node(value,self.top)

    def pop(self):
        if self.top is None:
            return None
        topNode = self.top
        self.top = self.top.next
        return topNode.item

    def is_empty(self):
        return self.top is None

class Queue():
    def __init__(self):
        self.front = None
    def push(self,value):
        if not self.front:
            self.front = Node(value,None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value,None)

        return

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None

def test_node():
    #보장한다 아이템의 값이 1
    assert Node(1,None).item == 1

def test_stack():
    """스택은 3가지 기능을 요구
    1.push
    2. pop
    3. is_empty
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

def test_queue():
    """스택은 3가지 기능을 요구
    1.push
    2. pop
    3. is_empty
    """
    queue = Queue()
    queue.push(1)


test_node()
test_stack()
test_queue()
# if __name__ == '__main_-':

