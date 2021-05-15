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
    # def dequeue(self):
    #     return self.queue.pop()
    def popFromLeft(self):
        tmp = self.queue[0]
        del(self.queue[0])
        return tmp
    def printQueue(self):
        print(self.queue)

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)

# print(q.popFromLeft())
# q.printQueue()

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

# print(n0.__dict__, n2.__dict__, n1.__dict__)

que = Queue()

def breadthFirst(node):
    que.enqueue(node)
    while len(que.queue) != 0:
        popedVal = que.popFromLeft()
        print(popedVal.data)
        if popedVal.leftChild is not None:
            que.enqueue(popedVal.leftChild)
        if popedVal.rightChild is not None:
            que.enqueue(popedVal.rightChild)

breadthFirst(n0)

