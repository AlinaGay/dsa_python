class Queue:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def enqueue(self, x: int):
        self.list.append(x)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop(0) 

    def last(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list[len(self.list)-1]                      

class MyStack:
    def __init__(self):
        self.inQueue = Queue()
        self.outQueue = Queue()

    def push(self, x: int) -> None:
      while len(self.inQueue):
        self.outQueue.enqueue(self.inQueue.dequeue())
      self.outQueue.enqueue(x)
      while len(self.outQueue):
        self.inQueue.enqueue(self.outQueue.dequeue())

    def pop(self) -> int:
        return self.inQueue.dequeue() 

    def top(self) -> int:
        return self.inQueue.last()  

    def empty(self) -> bool:
        if len(self.inQueue) == 0:
            return True
        return False    