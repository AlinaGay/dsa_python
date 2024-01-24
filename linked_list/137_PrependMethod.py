class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0    

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1

new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.prepend(20)
print(new_linked_list.head.value)      