class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self,value):
    new_node = Node(value)
    new_node.next = new_node
    self.head = new_node
    self.tail = new_node
    self.length = 1

  # def __init__(self): # Empty CSLL
  #   self.head = None
  #   self.tail = None
  #   self.length = 0  

cslinkedkist = CSLinkedList(10)
print(cslinkedkist.head.value)        