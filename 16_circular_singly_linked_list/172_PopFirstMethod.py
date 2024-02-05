class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self): 
    return str(self.value)   

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
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
  
  def pop_first(self):
    popped_node = self.head
    if self.length == 0:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
    else:  
      self.head = self.head.next
      self.tail.next = self.head
      popped_node.next = None
    self.length -= 1
    return popped_node


cslinkedkist = CSLinkedList() 
cslinkedkist.prepend(40)
cslinkedkist.prepend(30)
cslinkedkist.prepend(20)
cslinkedkist.prepend(10)
print(cslinkedkist) 
print(cslinkedkist.pop_first()) 
print(cslinkedkist)      
