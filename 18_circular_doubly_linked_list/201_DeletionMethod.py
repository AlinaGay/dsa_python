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

  def insertCDLL(self, value, location):
    if self.head is None:
      return "The CDLL does not exist"
    else:
      newNode = Node(value)
      if location == 0:
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.head = newNode
        self.tail.next = newNode
      elif location == 1:
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.tail.next = newNode
        self.tail = newNode
      else:
        tempNode = self.head
        index = 0
        while index < location-1:
          tempNode = tempNode.next
          index += 1
        newNode.next = tempNode.next
        newNode.prev = tempNode
        newNode.next.prev = newNode
        tempNode.next = newNode
      return "The node has been successfully inseted"
  
  def deleteNode(self, location):
    if self.head is None:
      print("There is not any node to delete")
    elif self.head == self.tail:
      self.head.prev = None
      self.head.next = None
      self.head = None
      self.tail = None
      print("The one element was deleted")  
    else:
      if location == 0:
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
      elif location == -1:
        self.tail = self.tail.prev
        self.tail.next = self.head 
        self.head.prev = self.tail
      else:
        curNode = self.head
        index = 0
        while index < location -1:
          curNode = curNode.next
          index += 1   
        curNode.next = curNode.next.next
        curNode.next.prev = curNode
      print("The node has been successfully deleted")    

  
new_list = CircularDoblyLinkedList()

new_list.createCDLL(10)
new_list.insertCDLL(0, 0)
new_list.insertCDLL(1, 1)
new_list.insertCDLL(2, 2)
new_list.insertCDLL(3, 3)
print([node.value for node in  new_list])
new_list.deleteNode(3)
print([node.value for node in  new_list])