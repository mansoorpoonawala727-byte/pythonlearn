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

def tree_height(root):
    if root is None:
        return -1
    else:
        height = 1 + max(tree_height(root.left), tree_height(root.right))
        return height

root = None
for num in [5, 3, 8, 1, 4, 9]:
    root = insert(root, num)

print(tree_height(root))