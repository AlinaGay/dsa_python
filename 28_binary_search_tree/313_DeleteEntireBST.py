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

def deleteBST(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "The BST has been successfully deleted"

new_BST = BSTNode(90)
insertNode(new_BST, 80)  
insertNode(new_BST, 100) 
insertNode(new_BST, 70)  
insertNode(new_BST, 85)
insertNode(new_BST, 95)  
insertNode(new_BST, 110)
print(deleteBST(new_BST))  