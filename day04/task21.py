class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_length(head):
    count=0
    current=head
    while current:
        current=current.next
        count+=1
    return count    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(linked_list_length(n1))  
print(linked_list_length(n3))  
print(linked_list_length(None)) 