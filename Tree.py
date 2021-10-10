class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add(self,data):
        if(data>self.data):
            if(self.right):
                self.right.add(data)
            else:
                self.right=BinaryTree(data)
        else:
            if(self.left):
                self.left.add(data)
            else:
                self.left=BinaryTree(data)

    def inorder(self):
        if(self.left):
            self.left.inorder()
        print(self.data,end=" ")
        if(self.right):
            self.right.inorder()
    def postorder(self):
        if(self.left):
            self.left.postorder()
        if(self.right):
            self.right.postorder()
        print(self.data,end=" ")
    def preorder(self):
        print(self.data,end=" ")
        if(self.left):
            self.left.preorder()
        if(self.right):
            self.right.preorder()

    def max(self):
        if(self.right):
            self.right.max()
        if(self.right==None):
            print(self.data)

    def min(self):
        if(self.left):
            self.left.min()
        if(self.left==None):
            print(self.data)

k=BinaryTree(10)
k.add(20)
k.add(30)
k.add(40)
k.add(5)
k.add(6)
k.inorder()
print("")
k.preorder()
print("")
k.postorder()
print("")
k.max()
print("")
k.min()
