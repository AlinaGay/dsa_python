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

