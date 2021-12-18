from itertools import permutations

def getAffectedNodeLeftOf(node):
    root = node
    while root.parent.left == root:
        root = root.parent
        if root.parent == None:
            return node.left
    ptr = root.parent.left
    while ptr.value == None:
        ptr = ptr.right
    return ptr

def getAffectedNodedRightOf(node):
    root = node
    while root.parent.right == root:
        root = root.parent
        if root.parent == None:
            return node.right
    ptr = root.parent.right
    while ptr.value == None:
        ptr = ptr.left
    return ptr

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None

    def split(self):
        if self.value == None:
            return  self.left.split() or self.right.split()
        if self.value < 10:
            return False
        self.right = TreeNode()
        self.right.value = self.value//2 + self.value % 2
        self.right.parent = self
        self.left = TreeNode()
        self.left.value = self.value//2
        self.left.parent = self
        self.value = None
        return True

    def explode(self):
        if not self.left or not self.right:
            return False
        if self.left.value == None or self.right.value == None:
            return self.left.explode() or self.right.explode()
        count = 0
        tmpPtr = self
        while count < 4:
            tmpPtr = tmpPtr.parent
            if not tmpPtr:
                return False
            count += 1
        explodeLeft = getAffectedNodeLeftOf(self)
        if explodeLeft != self.left:
            explodeLeft.value  += self.left.value
        explodeRight = getAffectedNodedRightOf(self)
        if explodeRight != self.right:
            explodeRight.value += self.right.value
        self.value = 0
        self.right = None
        self.left = None
        return True

def treeFromList(l):
    if type(l) == list:
        node = TreeNode()
        left, right = treeFromList(l[0]), treeFromList(l[1])
        node.left = left
        node.right = right
        left.parent = node
        right.parent = node
        return node
    else:
        node = TreeNode()
        node.value = int(l)
        return node

def reduceTree(curTree):
    while True:
        if curTree.explode():
            continue
        if not curTree.split():
            break

def magnitude(node):
    if node.value != None:
        return node.value
    return 3*magnitude(node.left) + 2*magnitude(node.right)

def toString(tree):
    if tree.value != None:
        return str(tree.value)
    return '[' + toString(tree.left) +  ', ' + toString(tree.right) + ']'

def toList(root):
    return eval(toString(root))

def partOne():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        result = None
        for x in lines:
            x = treeFromList(eval(x.strip()))
            reduceTree(x)
            result = treeFromList([toList(result)] + [toList(x)]) if result else x
            reduceTree(result)
        return magnitude(result)


def partTwo():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        maxRes = 0
        for z in permutations(lines, 2):
            result = None
            for x in z:
                x = treeFromList(eval(x.strip()))
                reduceTree(x)
                result = treeFromList([toList(result)] + [toList(x)]) if result else x
                reduceTree(result)
            maxRes = max(magnitude(result), maxRes)
        return maxRes

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
