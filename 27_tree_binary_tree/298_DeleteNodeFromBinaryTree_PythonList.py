class BinaryTree:
  def __init__(self, size):
    self.customList = size * [None]
    self.lastUsedIndex = 0
    self.maxSize = size

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return "The BT is full"
    self.customList[self.lastUsedIndex + 1] = value
    self.lastUsedIndex += 1
    return "The value has been successfully inserted"  
  
  def searchNode(self, nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i] == nodeValue:
        return "Success"
    return "Not found"
  
  def levelOrderTraversal(self, index):
    for i in range(index, self.lastUsedIndex + 1):
      print(self.customList[i])

  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return "There is not any node to delete"
    for i in range(1, self.lastUsedIndex+1):
      if self.customList[i] == value:
        self.customList[i] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return "The node has been successfully deleted"

customBT = BinaryTree(8)    
customBT.insertNode("Drinks")
customBT.insertNode("Hot")
customBT.insertNode("Cold")
customBT.insertNode("Tea")
customBT.insertNode("Coffee")
customBT.insertNode("Cola")
customBT.levelOrderTraversal(1)
customBT.deleteNode("Tea")
print("---------------------------------")
customBT.levelOrderTraversal(1)