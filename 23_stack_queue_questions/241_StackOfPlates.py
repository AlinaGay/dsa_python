class PlateStack():
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def __str__(self):
    return self.stacks

  def push(self, item):
    if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity: # if the last stack is not full
      self.stacks[-1].append(item) # add the new item at the end of the last stack
    else:
      self.stacks.append([item]) #create and add new stack with new item

  def pop(self):
    while len(self.stacks) and len(self.stacks[-1]) == 0: # while stacks exist and all of them full 
      self.stacks.pop() # delete the last elemnet whole stack
    if len(self.stacks) == 0: # if stacks do not exist 
      return None
    else:
      return self.stacks[-1].pop() # delete the last element of the last stack

  def pop_at(self, stackNumber):
    if len(self.stacks[stackNumber]) > 0: # if the concrete stack exists
      return self.stacks[stackNumber].pop() # delete the last element of this stack
    else:
      return None

customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop())
print(customStack.pop_at(0))

