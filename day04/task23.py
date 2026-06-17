class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
         return True
    return False
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5    
print(has_cycle(n1))    
n5.next = n3
print(has_cycle(n1))  