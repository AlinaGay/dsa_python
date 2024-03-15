class Node():
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    string = str(self.value)
    if self.next:
      string = ','+str(self.next)
    return string

class Stack():
  def __init__(self):
    self.top = None
    self.minNode = None

  def min(self): # works as min function
    if not self.minNode:
      return None
    return self.minNode.value

  def push(self, item):
    if self.minNode and (self.minNode.value < item):
      self.minNode = Node(value=self.minNode.value, next=self.minNode) # minNode refers to itself
    else:
      self.minNode = Node(value=item, next=self.minNode) # minNode refers to the previous minimum
    self.top = Node(value=item, next=self.top) # top refers to the previous top

  def pop(self):
    if not self.top:
      return None
    self.minNode = self.minNode.next
    item = self.top.value
    self.top = self.top.next
    return item
  
customStack = Stack()
customStack.push(6)
customStack.push(3)
print(customStack.min())
customStack.push(5)
customStack.push(0)
print(customStack)
print(customStack.min())
print(customStack.pop())

