
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def find_middle(self):
      slow = self.head
      fast = self.head
      while fast is not None and fast.next is not None:
          slow = slow.next
          print(f'slow {slow.value}')
          fast = fast.next.next
          print(f'fast {fast.value}')
      return slow.value

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.append(60)
new_linked_list.append(70)
new_linked_list.append(80)
new_linked_list.append(90)
print(new_linked_list)
print(new_linked_list.find_middle())