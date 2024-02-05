class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self): 
    return self.value   

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

  def traverse(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next
      if current.next == self.head:
        break  

  def search(self,target):
    current = self.head
    while current is not None:
      if current.value == target:
        return True
      current = current.next
      if current.next == self.head:
        break
    return False  
  
  def get(self, index):
    if index == -1:
      return self.tail
    if index < -1 or index >= self.length:
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current
  
  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False


cslinkedkist = CSLinkedList() 
cslinkedkist.prepend(40)
cslinkedkist.prepend(30)
cslinkedkist.prepend(20)
cslinkedkist.prepend(10)
print(cslinkedkist) 
cslinkedkist.set_value(1, 100) 
print(cslinkedkist)      
