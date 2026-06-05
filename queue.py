class queue:
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0

    def enqueue(self,x):
        self.items.append(x) # O(1) time complexity

    def dequeue(self):
        if self.isempty():
            raise Exception("Queue is empty")
        else:
            return self.items.pop(0) # O(n) time complexity

q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())