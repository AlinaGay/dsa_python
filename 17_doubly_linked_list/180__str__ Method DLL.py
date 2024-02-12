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

  def append(self, value):  
    new_node = Node(value)
    if not self.head:
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1    

new_list = DoublyLinkedList()
new_list.append(10)
new_list.append(20)
new_list.append(30)
new_list.append(40)
new_list.append(50)
print(new_list)    