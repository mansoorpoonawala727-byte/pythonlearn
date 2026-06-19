class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
     if root is None:
        return TreeNode(val)   
    
     if val < root.val:
        root.left = insert(root.left, val)  
     else:
        root.right = insert(root.right, val) 
    
     return root

def search(root, val):
    if root is None:
        return False             
    
    if root.val == val:
        return True                
    
    if val < root.val:
        return search(root.left, val)  
    else:
        return search(root.right, val)  

root = None
for num in [5, 3, 8, 1, 4, 9]:
    root = insert(root, num)

print(search(root, 4))  
print(search(root, 7))  