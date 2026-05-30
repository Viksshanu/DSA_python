# Node class
# Each node stores:
# 1. data
# 2. address of next node

class node:

    def __init__(self, info, next=None):

        # Store data
        self.data = info

        # Store next node address
        self.next = next


# Linked List class
class linkedlist:

    def __init__(self, head=None):

        # Initially head is None
        self.head = head

    # -----------------------------------
    # Insert node at END
    # -----------------------------------
    def insertatend(self, value):

        # Create new node
        temp = node(value)

        # If list already exists
        if self.head != None:

            # Start traversal from head
            t1 = self.head

            # Move until last node
            while t1.next != None:
                t1 = t1.next

            # Connect last node to new node
            t1.next = temp

        # If list is empty
        else:
            self.head = temp

    # -----------------------------------
    # Insert node at BEGINNING
    # -----------------------------------
    def insertatbeg(self, value):

        # Create new node
        temp = node(value)

        # New node points to old head
        temp.next = self.head

        # Move head to new node
        self.head = temp

    # -----------------------------------
    # Insert node AFTER a given value
    # Example:
    # insertatmid(12,5)
    # inserts 12 after 5
    # -----------------------------------
    def insertatmid(self, value, x):

        # Start from head
        temp = self.head

        # Create new node
        t1 = node(value)

        # Traverse list
        while temp != None:

            # If target value found
            if temp.data == x:

                # New node points to next node
                t1.next = temp.next

                # Current node points to new node
                temp.next = t1

                # Stop after insertion
                break

            # Move to next node
            temp = temp.next

    # -----------------------------------
    # Delete a node by value
    # -----------------------------------
    def delete(self, value):

        # Start from head
        t1 = self.head

        # Previous pointer
        prev = None

        # If first node itself contains value
        if t1 != None and t1.data == value:

            # Move head to next node
            self.head = t1.next

            return

        # Traverse list
        while t1 != None:

            # Value found
            if t1.data == value:

                # Remove node
                prev.next = t1.next

                return

            # Move pointers
            prev = t1
            t1 = t1.next

    # -----------------------------------
    # Print linked list
    # -----------------------------------
    def printll(self):

        t1 = self.head

        while t1 != None:

            print(t1.data, end=" ")

            t1 = t1.next


# Create object
obj = linkedlist()

# Insert at beginning
obj.insertatbeg(5)

# Insert at end
obj.insertatend(10)
obj.insertatend(15)
obj.insertatend(20)
obj.insertatend(30)

# Insert 12 after 10
obj.insertatmid(12, 10)

# Delete operations
obj.delete(30)
obj.delete(5)

# Print final list
obj.printll()