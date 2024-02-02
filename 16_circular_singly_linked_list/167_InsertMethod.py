class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self) -> str:
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      temp_node = temp_node.next
      if temp_node == self.head:
        break
      result += '->' 
    return result 

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      self.tail.next = new_node
    self.length += 1

  def insert(self, index, value):
    new_node = Node(value)
    temp_node = self.head
    for _ in range(index-1):
      temp_node = temp_node.next
    new_node.next = temp_node.next
    temp_node.next = new_node
    self.length += 1    

cslinkedkist = CSLinkedList() 
cslinkedkist.prepend(40)
cslinkedkist.prepend(30)
cslinkedkist.prepend(20)
cslinkedkist.prepend(10) 
cslinkedkist.insert(2, 90)
print(cslinkedkist)  
print(cslinkedkist.length)         
