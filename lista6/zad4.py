class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack += [item]

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return(str(self.stack))

class BinaryTree:

    def __init__(self,rootObj, num=1):
        self.key = rootObj
        self.key_num = num
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            if self.leftChild.key == newNode:
                self.leftChild.key_num += 1
            else:
                t = BinaryTree(newNode)
                t.leftChild = self.leftChild
                self.leftChild = t
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            if self.rightChild.key == newNode:
                self.rightChild.key_num += 1
            else:
                t = BinaryTree(newNode)
                t.rightChild = self.rightChild
                self.rightChild = t     
            
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key 

def to_string(tree:BinaryTree, string=''):
    """Create a string from the expression tree.
    
    @param tree:(BinaryTree) expression tree
    
    @return:(str) expression as string"""
    if tree != None:
        if tree.key not in ['sin', 'cos', 'log', 'exp']:
            string += '( '
            string += f'{to_string(tree.leftChild)} '
            string += f'{tree.key} '
            string += f'{to_string(tree.rightChild)} '
            string += ') '
        else:
            string += f'{tree.key} '
            string += f'{to_string(tree.leftChild)} '
    return string

def deriv(tree:BinaryTree):
    """Create expression derived tree.

    @param tree:(BinaryTree) expression tree

    @return:(BinaryTree) expression derived tree"""
    new_tree = BinaryTree('')
    if tree.key == '+':
        new_tree.key = '+'
        new_tree.leftChild = deriv(tree.leftChild)
        new_tree.rightChild = deriv(tree.rightChild)
    if tree.key == '-':
        new_tree.key = '-'
        new_tree.leftChild = deriv(tree.leftChild)
        new_tree.rightChild = deriv(tree.rightChild)
    if tree.key == '*':
        new_tree.key = '+'
        new_tree.leftChild = BinaryTree('*')
        new_tree.rightChild = BinaryTree('*')
        new_tree.leftChild.leftChild = deriv(tree.leftChild)
        new_tree.leftChild.rightChild = tree.rightChild
        new_tree.rightChild.leftChild = tree.leftChild
        new_tree.rightChild.rightChild = deriv(tree.rightChild)
    if tree.key == '/':
        new_tree.key = '/'
        new_tree.leftChild = BinaryTree('+')
        new_tree.leftChild.leftChild = BinaryTree('*')
        new_tree.leftChild.rightChild = BinaryTree('*')
        new_tree.leftChild.leftChild.leftChild = deriv(tree.leftChild)
        new_tree.leftChild.leftChild.rightChild = tree.rightChild
        new_tree.leftChild.rightChild.leftChild = tree.leftChild
        new_tree.leftChild.rightChild.rightChild = deriv(tree.rightChild)
        new_tree.rightChild = BinaryTree('*')
        new_tree.rightChild.leftChild = tree.rightChild
        new_tree.rightChild.rightChild = tree.rightChild
    if tree.key == '**':
        new_tree.key = '*'
        new_tree.leftChild = tree.rightChild
        new_tree.rightChild = BinaryTree('**')
        new_tree.rightChild.leftChild = tree.leftChild
        new_tree.rightChild.rightChild = BinaryTree(f'{int(tree.rightChild.key) - 1}')
    if tree.key == 'sin':
        new_tree.key = '*'
        new_tree.leftChild = BinaryTree('cos')
        new_tree.leftChild.leftChild = tree.leftChild
        new_tree.rightChild = deriv(tree.leftChild)
    if tree.key == 'cos':
        new_tree.key = '*'
        new_tree.leftChild = BinaryTree('*')
        new_tree.leftChild.leftChild = BinaryTree('-1')
        new_tree.leftChild.rightChild = BinaryTree('sin')
        new_tree.leftChild.rightChild.leftChild = tree.leftChild
        new_tree.rightChild = deriv(tree.leftChild)
    if tree.key == 'log':
        new_tree.key = '*'
        new_tree.leftChild = BinaryTree('/')
        new_tree.leftChild.leftChild = BinaryTree('1')
        new_tree.leftChild.rightChild = tree.leftChild
        new_tree.rightChild = deriv(tree.leftChild)
    if tree.key == 'exp':
        new_tree.key = '*'
        new_tree.leftChild = BinaryTree('exp')
        new_tree.leftChild.leftChild = tree.leftChild
        new_tree.rightChild = deriv(tree.leftChild)
    if tree.key == 'x':
        new_tree.key = '1'
    if tree.key in ['-1','-2','-3','-4','-5','-6','-7','-8','-9,','0','1','2','3','4','5','6','7','8','9']:
        new_tree.key = '0'
    return new_tree

def buildParseTree(fpexp):
    """Create the expression tree.
    
    @param fpexp:(str) expression
    
    @return:(BinaryTree) expression tree"""
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', '**', ')', 'sin', 'cos', 'log', 'exp']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', '**']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i in ['sin', 'cos', 'log', 'exp']:
            currentTree.setRootVal(i)
            currentTree.insertLeft('')
            #pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def deriv_string(string):
    """Compute the derivative of the expression.
    
    @param string:(str) expression to derivate
    
    @return:(str) derivated expression"""
    old_tree = buildParseTree(string)
    new_tree = deriv(old_tree)
    return to_string(new_tree)

print(deriv_string('( ( 2 * x ) + ( x ** 3 ) )'))