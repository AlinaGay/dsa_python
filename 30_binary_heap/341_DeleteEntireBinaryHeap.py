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

def heapifyTreeExtract(rootNode, index, heapType):
  leftIndex = index * 2
  rightIndex = index * 2 + 1
  swapChild = 0

  if rootNode.heapSize < leftIndex:
    return
  
  elif rootNode.heapSize == leftIndex:
    if heapType == "Min":
      if rootNode.cutomList[index] > rootNode.cutomList[leftIndex]:
        temp = rootNode.cutomList[index]
        rootNode.cutomList[index] = rootNode.cutomList[leftIndex]
        rootNode.cutomList[leftIndex] = temp
      return
    else:
      if rootNode.cutomList[index] < rootNode.cutomList[leftIndex]:
        temp = rootNode.cutomList[index]
        rootNode.cutomList[index] = rootNode.cutomList[leftIndex]
        rootNode.cutomList[leftIndex] = temp
      return
  else:
    if heapType == "Min":
      if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
        swapChild = leftIndex
      else:
        swapChild = rightIndex
      if rootNode.customList[index] > rootNode.customList[swapChild]:
        temp = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[swapChild]
        rootNode.customList[swapChild] = temp
    else:      
      if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
        swapChild = leftIndex
      else:
        swapChild = rightIndex
      if rootNode.customList[index] > rootNode.customList[swapChild]:
        temp = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[swapChild]
        rootNode.customList[swapChild] = temp
  heapifyTreeExtract(rootNode, swapChild, heapType)    

def extractNode(rootNode, heapType):
  if rootNode.heapSize == 0:
    return
  else:
    extractNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractNode      

def deleteEntireBH(rootNode):
  rootNode.customList = None

newBH = Heap(5)
insertNode(newBH, 4, "Max")
insertNode(newBH, 5, "Max")
insertNode(newBH, 2, "Max")
insertNode(newBH, 1, "Max")
deleteEntireBH(newBH)
levelOrderTraversal(newBH) 