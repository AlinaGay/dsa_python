class AVLNode:
  def __init__(self, data):
    self.data = data 
    self.leftChild = None
    self.rightChild = None
    self.height = 1

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
    
def preOrderTraversal(rootNode):
  if not rootNode.data:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
  if not rootNode.data:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
  if not rootNode.data:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)

def levelOrderTraversal(rootNode):
  if not rootNode.data:
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

def searchNode(rootNode, nodeValue):
  if rootNode.data == nodeValue:
    print("The value is found")
  elif nodeValue < rootNode.data:
    if rootNode.leftChild.data == nodeValue:
      print("The value is found")
    else:
      searchNode(rootNode.leftChild, nodeValue)
  else:
    if rootNode.rightChild.data == nodeValue:
      print("The value is found")
    else:
      searchNode(rootNode.rightChild, nodeValue)    

def getHeight(rootNode):
  if not rootNode:
    return 0
  return rootNode.height

def rightRotate(disbalanceNode):
  newRoot = disbalanceNode.leftChild
  disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
  newRoot.rightChild = disbalanceNode
  disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
  newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
  return newRoot

def leftRotate(disbalanceNode):
  newRoot = disbalanceNode.rightChild
  disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
  newRoot.leftChild = disbalanceNode
  disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
  newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
  return newRoot

def getBalance(rootNode):
  if not rootNode:
    return 0
  return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
  if not rootNode:
    return AVLNode(nodeValue)
  elif nodeValue < rootNode.data:
    rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
  else:
    rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

  rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
  balance = getBalance(rootNode)

  if balance > 1 and nodeValue < rootNode.leftChild.data:
    return rightRotate(rootNode)
  if balance > 1 and nodeValue > rootNode.leftChild.data:
    rootNode.leftChild = leftRotate(rootNode.leftChild)
    return rightRotate(rootNode)
  if balance < -1 and nodeValue > rootNode.rightChild.data:
    return leftRotate(rootNode)
  if balance < -1 and nodeValue < rootNode.rightChild.data:
    rootNode.rightChild = rightRotate(rootNode.rightChild)
    return leftRotate(rootNode)
  return rootNode

def deleteAVL(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "The AVL has been successfully deleted"

newAVl = AVLNode(5)
newAVl = insertNode(newAVl, 10)
newAVl = insertNode(newAVl, 15)
newAVl = insertNode(newAVl, 20)
levelOrderTraversal(newAVl)
print("--------------------------------------")
print(deleteAVL(newAVl))
