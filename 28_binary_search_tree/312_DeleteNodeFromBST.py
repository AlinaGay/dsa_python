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

def minValueNode(bstNode):
  current = bstNode
  while (current.leftChild is not None):
    current = current.leftChild
  return current

def deleteNode(rootNode, nodeValue):
  if rootNode is None:
    return rootNode
  if nodeValue < rootNode.data:
    rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
  elif nodeValue > rootNode.data:
    rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
  else:
    if rootNode.leftChild is None:
      temp = rootNode.rightChild
      rootNode = None
      return temp
    if rootNode.rightChild is None:
      temp = rootNode.leftChild
      rootNode = None
      return temp

    temp = minValueNode(rootNode.rightChild)
    rootNode.data = temp.data
    rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

  return rootNode  

new_BST = BSTNode(90)
insertNode(new_BST, 80)  
insertNode(new_BST, 100) 
insertNode(new_BST, 70)  
insertNode(new_BST, 85)
insertNode(new_BST, 95)  
insertNode(new_BST, 110)
print(deleteNode(new_BST, 80))  