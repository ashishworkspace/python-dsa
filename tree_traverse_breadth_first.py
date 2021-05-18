# tree traversing level wise

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.insert(0, data)
    def popFromLeft(self):
        tmp = self.queue[0]
        del(self.queue[0])
        return tmp


n0 = TreeNode("/root")
n1 = TreeNode("/root/Desktop")
n2 = TreeNode("/root/Download")

n0.leftChild = n1
n0.rightChild = n2

n3 = TreeNode("/root/Download/file.png")
n4 = TreeNode("/root/Download/file2.rpm")

n2.leftChild = n3
n2.rightChild = n4

n5 = TreeNode("/root/Desktop/helloWorld.py")
n6 = TreeNode("/root/Desktop/vscode.exe")

n1.leftChild = n5
n1.rightChild = n6



que = Queue() # creating an object for Queue class

def breadthFirst(node):
    que.enqueue(node)
    while len(que.queue) != 0:                      # This Loop will run until the queue is empty
        popedVal = que.popFromLeft()                # popFromLeft() helps to pop an element from Left
        print(popedVal.data)
        if popedVal.leftChild != None:              # IF the Left Child Node is Not none then insert it into the queue. 
            que.enqueue(popedVal.leftChild)
        if popedVal.rightChild != None:
            que.enqueue(popedVal.rightChild)        # IF the Right Child Node is Not none then insert it into the queue.

breadthFirst(n0)

