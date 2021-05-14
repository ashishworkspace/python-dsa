class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



node1 = TreeNode(data="N1")
node2 = TreeNode(data="N2")
node3 = TreeNode(data="N3")
node1.leftChild = node2
node1.rightChild = node3

# print(node1.__dict__)

node4 = TreeNode(data="N4")
node5 = TreeNode(data="N5")
node2.leftChild = node4
node2.rightChild = node5

# print(node2.__dict__)

node6 = TreeNode(data="N6")
node7 = TreeNode(data="N7")
node4.leftChild = node6
node4.rightChild = node7

# print(node4.__dict__) 

node8 = TreeNode(data="N8")
node9 = TreeNode(data="N9")
node3.leftChild = node8
node3.rightChild = node9

# print(node3.__dict__)


# preorder traverse

print("PreOrder Traverse")
def preOrderTraversal(root_node):
    if root_node == None:
        pass
    else: 
        print(root_node.data, end="  ")
        preOrderTraversal(root_node.leftChild)
        preOrderTraversal(root_node.rightChild)

preOrderTraversal(node1)

#postorder traverse

print("\nPostOrder Traverse")
def postOrderTraversal(root_node):
    if root_node == None:
        pass
    else:
        postOrderTraversal(root_node.leftChild)
        postOrderTraversal(root_node.rightChild)
        print(root_node.data, end="  " )

postOrderTraversal(node1)