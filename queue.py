class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data): # used to inserst element at first position
                             # this means that when a new element is inserted in queue it will be at last of the queue
        self.queue.insert(0, data)
    def dequeue(self):       # used to remove last element in list
        self.queue.pop()
    


integer = Queue() 


integer.enqueue(data=1)
integer.enqueue(data=5)
integer.enqueue(data=7)
integer.enqueue(data=1)
integer.enqueue(data=0)



print(integer.queue)

integer.dequeue()  # remove the last position in queue

print(integer.queue)

