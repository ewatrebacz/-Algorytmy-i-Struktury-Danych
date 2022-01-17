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