class AVLNode:
  def __init__(self, data):
    self.data = data 
    self.leftChild = None
    self.rightChild = None
    self.height = 1

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


newAVl = AVLNode(70)
node_50 = AVLNode(50) 
node_90 = AVLNode(90)
newAVl.leftChild = node_50
newAVl.rightChild = node_90
node_30 = AVLNode(30) 
node_60 = AVLNode(60)
node_80 = AVLNode(80)
node_100 = AVLNode(100)  
node_50.leftChild = node_30
node_50.rightChild = node_60 
node_90.leftChild = node_80
node_90.rightChild = node_100 
node_20 = AVLNode(20)
node_40 = AVLNode(40)            
node_30.leftChild = node_20
node_30.rightChild = node_40

