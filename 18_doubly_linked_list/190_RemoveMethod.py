class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value) 

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += ' <-> '
      temp_node = temp_node.next
    return result 
  
  def preppend(self, value):  
    new_node = Node(value)
    if not self.head:
      self.tail = new_node
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1  

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    elif index < self.length//2:
      current_node = self.head
      for _ in range(index):
         current_node = current_node.next
    else:
      current_node = self.tail
      for _ in range(self.length-1, index, -1):
        current_node = current_node.prev
    return current_node

  def pop_first(self):
    if not self.head:
      return None
    popped_node = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:  
      self.head = self.head.next
      self.head.prev = None
      popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
    if not self.head:
      return None
    popped_node = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
      popped_node.prev = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      popped_node.prev = None
    self.length -= 1
    return popped_node

  def remove(self, index):
    if index == 0:
      return self.pop_first()
    if index == self.length-1:
      return self.pop()
    if index < 0 or index >= self.length:
      return None
    else:
      popped_node = self.get(index)
      popped_node.prev.next = popped_node.next
      popped_node.next.prev = popped_node.prev
      popped_node.next = None
      popped_node.prev = None
    self.length -= 1
    return popped_node
    

new_list = DoublyLinkedList()
new_list.preppend(10)
new_list.preppend(20)
new_list.preppend(30)
new_list.preppend(40)
new_list.preppend(50)
print(new_list)  
print(new_list.remove(1))
print(new_list)   