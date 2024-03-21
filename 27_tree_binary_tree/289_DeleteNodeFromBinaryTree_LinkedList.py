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

  def peek(self):
    if self.isEmpty():
      return "There is not any node in the Queue"
    else:
      return self.linkedList.head
    
  def delete(self):
    self.linkedList.head = None
    self.linkedList.tail = None

class TreeNode:
  def __init__(self,data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBT = TreeNode("Drinks")  
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
      root = customQueue.dequeue()
      print(root.value.data)
      if (root.value.leftChild is not None):
        customQueue.enqueue(root.value.leftChild)
      if (root.value.rightChild is not None):
        customQueue.enqueue(root.value.rightChild)

def getDeepestNode(rootNode):
  if not rootNode:
    return
  else:
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
      root = customQueue.dequeue()
      if (root.value.leftChild is not None):
        customQueue.enqueue(root.value.leftChild)
      if (root.value.rightChild is not None):
        customQueue.enqueue(root.value.rightChild)
    deepestNode = root.value
    return deepestNode

def deleteDeepestNode(rootNode, dNode):
  if not rootNode:
    return
  else:
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
      root = customQueue.dequeue()
      if root.value is dNode:
        root.value = None
        return
      if root.value.rightChild:
        if root.value.rightChild is dNode:
          root.value.rightChild = None
          return
        else:
          customQueue.enqueue(root.value.rightChild)
      if root.value.leftChild:
        if root.value.leftChild is dNode:
          root.value.leftChild = None
          return
        else:
          customQueue.enqueue(root.value.leftChild)
            
def deleteNodeBT(rootNode, node):
  if not rootNode:
    return "The BT does not exist"
  else:
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
      root = customQueue.dequeue()
      if root.value.data == node:
        dNode = getDeepestNode(rootNode)
        root.value.data = dNode.data
        deleteDeepestNode(rootNode, dNode)
        return "The node has been successfully deleted"
      if (root.value.leftChild is not None):
        customQueue.enqueue(root.value.leftChild)
      if (root.value.rightChild is not None):
        customQueue.enqueue(root.value.rightChild)
    return "Failed to delete"     
     
deleteNodeBT(newBT, "Tea")
levelOrderTraversal(newBT)