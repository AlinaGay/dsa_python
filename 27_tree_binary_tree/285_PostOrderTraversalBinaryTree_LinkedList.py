class TreeNode:
  def __init__(self,data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBT = TreeNode("Drinks")  
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild) 
  print(rootNode.data)

postOrderTraversal(newBT)