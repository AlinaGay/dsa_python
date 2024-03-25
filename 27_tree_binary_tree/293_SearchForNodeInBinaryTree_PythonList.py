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

customBT = BinaryTree(8)    
customBT.insertNode("Drinks")
customBT.insertNode("Hot")
customBT.insertNode("Cold")
customBT.insertNode("Tea")
customBT.insertNode("Coffee")
customBT.insertNode("Cola")
print(customBT.searchNode("Hot"))
print(customBT.searchNode("Fanta"))