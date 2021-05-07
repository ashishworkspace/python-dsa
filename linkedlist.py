class LinkedList:
    def __init__(self, data):
        self.data = data
        self.nextNodeaddr = None

node1 = LinkedList(10)

node2 = LinkedList(20)

node3 = LinkedList(30)

start = node1
node1.nextNodeaddr = node2
node2.nextNodeaddr = node3

print(node1, node2, node3)
print("\n")
print(start, node1.__dict__, node2.__dict__, node3.__dict__ )

print(start.nextNodeaddr.nextNodeaddr)

while (start is not None):
    print(start.data, end=",")
    start = start.nextNodeaddr
    print(start)
