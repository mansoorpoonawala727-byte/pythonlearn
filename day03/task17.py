class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  
        current.next = prev         
        prev = current               
        current = next_node               
    
    return prev
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


new_head = reverse_linked_list(n1)


current = new_head
while current:
    print(current.val, end=" → ")
    current = current.next
print("None")