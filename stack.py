class stack:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)

    def push(self,x):
        # self.s.append(x)    # O(1) time complexity

        self.s.insert(0,x)   # O(n) time complexity both are used to insert an element at the end of the stack but the first one is more efficient

    def peek(self):
        if self.s==0:
            raise Exception("Stack is empty")
        else:
            return self.s[0]

    def pop(self):
        if self.s==0:
            raise Exception("Stack is empty")

        else:
             return self.s.pop(0)  # O(n) time complexity both are used to remove an element from the end of the stack but the first one is more efficient
        
stk=stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.peek())  # Output: 3
# print(stk.pop())   # Output: 3
# print(stk.peek())  # Output: 2     
  