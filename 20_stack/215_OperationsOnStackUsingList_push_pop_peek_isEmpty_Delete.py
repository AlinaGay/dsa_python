class Stack:
  def __init__(self):
    self.list = []

  def __str__(self):
    values = self.list.reverse()
    values = [str(x) for x in self.list]
    return '\n'.join(values)

  def isEmpty(self):
      if self.list == []:
        return True
      else:
        return False
      
  def push(self, value):
    self.list.append(value)
    return "The element has been successfully inserted" 

  def pop(self):
    if self.isEmpty():
      return "There is not any element in he stack"
    else:
      return self.list.pop() 

  def peek(self):
    if self.isEmpty():
      return "There is not any element in he stack"
    else:
      return self.list[len(self.list)-1]
    
  def delete(self):
    self.list = None  
      
customStack = Stack()
print(customStack.isEmpty()) 
print('----------------') 
print(customStack.push(1)) 
print(customStack.push(2))
print(customStack.push(3)) 
print(customStack)  
print('----------------')  
print(customStack.pop())
print('----------------') 
print(customStack) 
print('----------------')  
print(customStack.peek())
print('----------------') 
print(customStack.delete())