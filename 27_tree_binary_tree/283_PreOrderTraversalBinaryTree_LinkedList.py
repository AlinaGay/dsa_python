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

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)    



preOrderTraversal(newTree)