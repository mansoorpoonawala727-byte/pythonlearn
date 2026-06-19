class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
       
         if root is None:       
             return []
    
         left = inorder(root.left)    
         right = inorder(root.right) 
         return left + [root.val] + right
def preorder(root):
        if root is None:       
             return []
    
        left = preorder(root.left)    
        right = preorder(root.right) 
        return [root.val] + left + right
   
         
def postorder(root):
        if root is None:       
             return []
    
        left = postorder(root.left)    
        right = postorder(root.right) 
        return left + right + [root.val]
   
         


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(inorder(root))   
print(preorder(root))  
print(postorder(root)) 