class node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insertatend(self, value):

        temp = node(value)

        if self.head != None:

            t1 = self.head

            while t1.next != None:
                t1 = t1.next

            t1.next = temp

        else:
            self.head = temp
            
    def insertatbeg(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp
        

    def printll(self):

        t1 = self.head

        while t1 != None:
            print(t1.data, end=" ")
            t1 = t1.next


obj = linkedlist()
obj=linkedlist()
obj=insertatbeg(5)
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)

obj.printll()