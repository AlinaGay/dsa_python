class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      new_node.next = new_node
    else:
      self.tail.next = new_node
      new_node.next = self.head
      self.tail = new_node
    self.length += 1 

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

cslinkedkist = CSLinkedList() 
cslinkedkist.append(10)
cslinkedkist.append(20)
cslinkedkist.append(30)
cslinkedkist.append(40)
cslinkedkist.append(50)
cslinkedkist.append(60)
print(cslinkedkist)      
