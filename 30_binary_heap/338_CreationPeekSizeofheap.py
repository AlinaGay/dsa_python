class Heap:
  def __init__(self,size):
    self.customList = (size + 1) * [None]
    self.heapSize = 0
    self.maxSize = size + 1

newBH = Heap(5)

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

print(peekOfHeap(newBH))
print(sizeOfHeap(newBH)) 