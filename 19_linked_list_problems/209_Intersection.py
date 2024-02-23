from random import randint

class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)

class LinkedList:
  def __init__(self,values=None):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    values = [str(x.value) for x in self]
    return ' -> '.join(values)

  def __len__(self):
    result = 0
    node = self.head
    while node:
      result += 1
      node = node.next
    return result   

  def add(self, value):
    if self.head is None:
      newNode = Node(value)
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next
    return self.tail

  def generate(self,n,min_value,max_value):
    self.head = None
    self.tail = None
    for i in range(n):
      self.add(randint(min_value,max_value))
    return self  

def intersection(LLA,LLB):
  if LLA.tail is not LLB.tail:
    return False
  
  lenA = len(LLA)
  lenB = len(LLB)

  shorter = LLA if lenA < lenB else LLB
  longer = LLB if lenA < lenB else LLA

  diff = len(longer) - len(shorter)
  longerNode = longer.head
  shorterNode = shorter.head

  for i in range(diff):
    longerNode = longerNode.next

  while shorterNode is not longerNode:
    shorterNode = shorterNode.next
    longerNode = longerNode.next

  return longerNode

def addSameNode(LLA,LLB,value):
  tempNode = Node(value)
  LLA.tail.next = tempNode
  LLA.tail = tempNode
  LLB.tail.next = tempNode
  LLB.tail = tempNode

LLA = LinkedList()
LLA.generate(3,0,10)

LLB = LinkedList()
LLB.generate(4,0,10)

addSameNode(LLA,LLB,11)
addSameNode(LLA,LLB,14)
      
print(LLA)
print(LLB)
print(intersection(LLA,LLB))

