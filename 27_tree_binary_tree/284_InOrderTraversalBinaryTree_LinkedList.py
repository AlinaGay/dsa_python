class TreeNode:
  def __init__(self,data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newTree = TreeNode("Drinks")  
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newTree.leftChild = leftChild
newTree.rightChild = rightChild

def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)    

inOrderTraversal(newTree)