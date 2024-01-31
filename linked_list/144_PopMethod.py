class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0    

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1 

  def insert(self, index, value):
    new_node = Node(value)
    if index < 0 or index > self.length:
      return False
    elif self.length == 0:
      self.head = new_node
      self.tail = new_node
    elif index == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      temp_node = self.head
      for _ in range(index-1):
        temp_node = temp_node.next
      new_node.next = temp_node.next
      temp_node.next = new_node
    self.length += 1
    
  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += '->'
      temp_node = temp_node.next 
    return result 
  
  def traverse(self):
    current = self.head
    while current is not None:
      print(current.value) 
      current = current.next  

  def search(self, target):
    current = self.head
    index = 0
    while current is not None:
      if current.value == target:
        return index
      current = current.next
      index += 1
    return -1  
  
  def get(self, index):
    if index == -1:
      return self.tail
    if index < -1 or index > self.length:
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current 
  
  def set(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
  
  def pop(self):
    if self.length == 0:
      return None
    popped_node = self.head
    if self.length == 1:
      self.tail = self.head = None
    else:  
      temp = self.head
      while temp.next is not self.tail:
        temp = temp.next
      self.tail = temp
      temp.next = None  
    self.length -= 1
    return popped_node

new_linked_list = LinkedList()
new_linked_list.insert(0,60)
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
      