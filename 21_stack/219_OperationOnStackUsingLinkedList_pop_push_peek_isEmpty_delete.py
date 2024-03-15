class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)  

class LinkedList:
  def __init__(self):
    self.head = None    

class Stack:
  def __init__(self):
    self.LinkedList = LinkedList()

  def __str__(self):
    temp_node = self.LinkedList.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += '->'
      temp_node = temp_node.next
    return result        

  def isEmpty(self):
    if self.LinkedList.head == None:
      return True
    else:
      return False

  def push(self, value):
    node = Node(value)
    node.next = self.LinkedList.head
    self.LinkedList.head = node

  def pop(self):
    if self.isEmpty():
      return "There is not any element in the stack"
    else:
      nodeValue = self.LinkedList.head
      self.LinkedList.head = self.LinkedList.head.next
      return nodeValue

  def peek(self):
    if self.isEmpty():
      return "There is not any element in the stack"
    else:
      nodeValue = self.LinkedList.head
      return nodeValue
    
  def delete(self):
    self.LinkedList.head = None  
    

customStack = Stack() 
print(customStack.isEmpty())
print('----------------')  
customStack.push(1) 
customStack.push(2) 
customStack.push(3) 
print(customStack)
print('----------------') 
print(customStack.pop())
print('----------------') 
print(customStack)
print('----------------') 
print(customStack.peek())
print('----------------') 
print(customStack.delete())
print('----------------') 
print(customStack.isEmpty())

