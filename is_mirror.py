class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

def createSample(inverse = False):
    tree = Node(0)
    right = left = tree
    for i in range(1,3):
        value = i * -1 if inverse else i
        right.right = Node(value)
        right = right.right
        left.left = Node(value * -1)
        left = left.left
    return tree

def printVerticalTree(node, level=0):
    if node:
        
        printVerticalTree(node.left, level + 1)
        
        printVerticalTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)


def verticalTree(node, level= 0):
    pass


def isMirror(tree1, tree2):
    if tree1 == None or tree2 == None:
        if tree1 == tree2:
            return True
        else:
            return False
    elif tree1.value != tree2.value:
        return False
    else:
        return isMirror(tree1.right, tree2.left) and isMirror(tree1.left, tree2.right)

def mirrorTree(tree):
    if tree == None:
        return None
    mirroredTree = Node(tree.value)
    mirroredTree.right = mirrorTree(tree.left)
    mirroredTree.left = mirrorTree(tree.right)
    return mirroredTree

tree1 = Node(1, Node(2, Node(4, Node(7)),Node(9)), Node(3, Node(5), Node(6)))
tree2 = Node(1, Node(3, Node(6), Node(5)), Node(2,Node(9), Node(4, None, Node(7))))
tree3 = mirrorTree(tree1)


printVerticalTree(tree1)
# printVerticalTree(tree3)

# print(isMirror(tree1, tree3))