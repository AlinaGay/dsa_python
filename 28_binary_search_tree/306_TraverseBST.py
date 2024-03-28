class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

class Queue:
  def __init__(self):
    self.linkedList = LinkedList()

  def __str__(self):
    values = [str(x) for x in self.linkedList]
    return ' '.join(values)

  def enqueue(self, value):
    newNode = Node(value)
    if self.linkedList.head == None:
      self.linkedList.head = newNode
      self.linkedList.tail = newNode
    else:
      self.linkedList.tail.next = newNode
      self.linkedList.tail = newNode     

  def isEmpty(self):
    if self.linkedList.head == None:
      return True
    else:
      return False
    
  def dequeue(self):
    if self.isEmpty():
      return "There is not any node in the Queue"
    else:
      tempNode = self.linkedList.head
      if self.linkedList.head == self.linkedList.tail:
        self.linkedList.head = None
        self.linkedList.tail = None
      else:
        self.linkedList.head = self.linkedList.head.next
      return tempNode  

class BSTNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

def insertNode(rootNode, nodeValue):
  if rootNode.data == None:
    rootNode.data = nodeValue
  elif nodeValue <= rootNode.data:
    if rootNode.leftChild is None:
      rootNode.leftChild = BSTNode(nodeValue) 
    else:
      insertNode(rootNode.leftChild, nodeValue)
  else:
    if rootNode.rightChild is None:
      rootNode.rightChild = BSTNode(nodeValue)
    else:
      insertNode(rootNode.rightChild, nodeValue)    
  return "The node has been successfully inserted"         

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)  

def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)  

def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data) 

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
      root = customQueue.dequeue()
      print(root.value.data)
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)  


new_BST = BSTNode(90)
insertNode(new_BST, 80)  
insertNode(new_BST, 100) 
insertNode(new_BST, 70)  
insertNode(new_BST, 85)
insertNode(new_BST, 95)  
insertNode(new_BST, 110)

preOrderTraversal(new_BST)
print("-------------------------")
inOrderTraversal(new_BST)
print("-------------------------")
postOrderTraversal(new_BST)
print("-------------------------")
levelOrderTraversal(new_BST)