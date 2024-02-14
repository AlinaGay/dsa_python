class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

class CircularDoblyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
      if node == self.tail.next:
        break

  def createCDLL(self, nodeValue):
    newNode = Node(nodeValue)
    self.head = newNode
    self.tail = newNode
    newNode.orev = newNode
    newNode.next = newNode
    return "The CDLL is created succesfully"      
  
new_list = CircularDoblyLinkedList()
new_list.createCDLL(10)
print(new_list.head.value)