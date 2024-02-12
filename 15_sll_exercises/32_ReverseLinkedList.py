class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
      def reverseList(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev, current = dummy, head
        while current:
            current.next = prev
            prev = current
            current = current.next
        print(dummy.next)        
        return dummy.next