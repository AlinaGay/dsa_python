class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current
        
    def reverse(self):
      prev_node = None
      current_node = self.head
      while current_node is not None: # current_node = 1
          next_node = current_node.next # next_node  = 2
          current_node.next = prev_node # current_node.next = None
          prev_node = current_node # prev_node = 1
          current_node = next_node # current_node = 2
      self.head, self.tail = self.tail, self.head

#Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5
#Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.reverse()
print(new_linked_list)