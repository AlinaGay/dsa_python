class MultiStack:
  def __init__(self, stacksize):
    self.numberstacks = 3
    self.custList = [0] * (stacksize * self.numberstacks) # fill the whole list(form several stacks) by 0
    self.sizes = [0] * self.numberstacks # keep in the list the size of each stack
    self.stacksize = stacksize # write as property capasity of each stack

  def isFull(self, stacknum):
    if self.sizes[stacknum] == self.stacksize: # check the size of conrete stack is full or not
      return True
    else:
      return False
    
  def isEmpty(self, stacknum):
    if self.sizes[stacknum] == 0: # check the size of concrete stack is empty or not
      return True
    else:
      return False  
    
  def indexOfTop(self, stacknum):
    offset = stacknum * self.stacksize # if it's imagined as matrix: offset is row number
    return offset + self.sizes[stacknum] - 1 #  if it's imagined as matrix: row number + colomn number -1

  def push(self, item, stacknum):
    if self.isFull(stacknum):
      return "The stack is full"
    else:
      self.sizes[stacknum] += 1 # increasing the size of concrete stack
      self.custList[self.indexOfTop(stacknum)] = item # put item in the top element of concrete stack

  def pop(self, stacknum):
    if self.isEmpty(stacknum):
      return "The stack is empty"
    else:
      value = self.custList[self.indexOfTop(stacknum)] # value is top element of concrete stack
      self.custList[self.indexOfTop(stacknum)] = 0 # put 0 to the top element of concrete stack
      self.sizes[stacknum] -= 1 # decreasing the size of concrete stack
      return value

  def peek(self, stacknum):
    if self.isEmpty(stacknum):
      return "Stack is empty"
    else:
      value = self.custList[self.indexOfTop(stacknum)] # value is top element of concrete stack       
      return value
    

customStack = MultiStack(6)
print(customStack.isFull(0))
print("---------------------")
print(customStack.isEmpty(1))
print("---------------------")
customStack.push(1, 0) 
customStack.push(2, 0)
customStack.push(3, 2)  
print(customStack.peek(2)) 
