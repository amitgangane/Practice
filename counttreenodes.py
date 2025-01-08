class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    if not root:
        return 0

    def getHeightLeft(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def getHeightRight(node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    left_height = getHeightLeft(root)
    right_height = getHeightRight(root)

    if left_height == right_height:
        return (1 << left_height) - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
