class Heap:
  def __init__(self,size):
    self.customList = (size + 1) * [None]
    self.heapSize = 0
    self.maxSize = size + 1

def peekOfHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.customList[1]
  
def sizeOfHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.heapSize
  
def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    for i in range(1, rootNode.heapSize + 1):
      print(rootNode.customList[i])  

def heapifyTreeInsert(rootNode, index, heapType):
  parentIndex = int(index/2)
  if index <= 1:
    return
  if heapType == "Min":
    if rootNode.customList[index] < rootNode.customList[parentIndex]:
      temp = rootNode.customList[index]
      rootNode.customList[index] = rootNode.customList[parentIndex]
      rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)
  elif heapType == "Max":
    if rootNode.customList[index] > rootNode.customList[parentIndex]:
      temp = rootNode.customList[index]
      rootNode.customList[index] = rootNode.customList[parentIndex]
      rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)  

def insertNode(rootNode, nodeValue, heapType):
  if rootNode.heapSize + 1 == rootNode.maxSize:
    return "The Binary Heap is Full"
  rootNode.customList[rootNode.heapSize + 1] = nodeValue
  rootNode.heapSize += 1
  heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
  return "The Value was successully inserted"    



newBH = Heap(5)
insertNode(newBH, 4, "Max")
insertNode(newBH, 5, "Max")
insertNode(newBH, 2, "Max")
insertNode(newBH, 1, "Max")
print(peekOfHeap(newBH))
print(sizeOfHeap(newBH))
levelOrderTraversal(newBH) 