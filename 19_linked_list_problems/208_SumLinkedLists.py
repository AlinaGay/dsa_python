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


def sumList(LLA, LLB):
  n1 = LLA.head
  n2 = LLB.head
  carry = 0
  LL = LinkedList()

  while n1 or n2:
    result = carry
    if n1:
      result += n1.value
      n1 = n1.next
    if n2:
      result += n2.value
      n2 = n2.next
    LL.add(int(result%10))
    carry = result/10

  return LL      

LLA = LinkedList()
LLA.add(7)
LLA.add(1)
LLA.add(6)
print(LLA)

LLB = LinkedList()
LLB.add(5)
LLB.add(9)
LLB.add(2)
print(LLB)

print(sumList(LLA,LLB))