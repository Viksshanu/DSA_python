# Node class for Doubly Linked List
class node:

    def __init__(self, data, prev=None, next=None):

        # Store data
        self.data = data

        # Pointer to previous node
        self.prev = prev

        # Pointer to next node
        self.next = next


# Doubly Linked List class
class doublyLL:

    def __init__(self):

        # Initially head is None
        self.head = None

    # -----------------------------------
    # Insert at END
    # -----------------------------------
    def insertatend(self, value):

        # Create new node
        temp = node(value)

        # If list is empty
        if self.head == None:

            self.head = temp
            return

        else:

            # Start from head
            t = self.head

            # Move to last node
            while t.next != None:
                t = t.next

            # Connect last node to new node
            t.next = temp

            # Connect new node back to last node
            temp.prev = t

    # -----------------------------------
    # Insert at BEGINNING
    # -----------------------------------
    def insertatbeg(self, value):

        # Create new node
        temp = node(value)

        # If list is empty
        if self.head == None:

            self.head = temp
            return

        else:

            # New node points to old head
            temp.next = self.head

            # Old head points back to new node
            self.head.prev = temp

            # Move head to new node
            self.head = temp

    # -----------------------------------
    # Insert AFTER a given position value
    # Example:
    # insertatmid(7,10)
    # inserts 7 after 10
    # -----------------------------------
    def insertatmid(self, value, pos):

        # Start traversal
        t = self.head

        # Traverse list
        while t != None:

            # If required node found
            if t.data == pos:
                break

            t = t.next

        # If position not found
        if t == None:
            print("Position value not found")
            return

        # Create new node
        temp = node(value)

        # New node points to next node
        temp.next = t.next

        # New node points back to current node
        temp.prev = t

        # If next node exists
        if t.next != None:

            # Next node points back to new node
            t.next.prev = temp

        # Current node points to new node
        t.next = temp

    # -----------------------------------
    # Display list
    # -----------------------------------
    def display(self):

        t = self.head

        while t != None:

            print(t.data, end=" ")

            t = t.next


# Create object
obj = doublyLL()

# Insert at end
obj.insertatend(5)
obj.insertatend(10)

# Insert at beginning
obj.insertatbeg(1)
obj.insertatbeg(0)

# Insert 7 after 10
obj.insertatmid(7, 10)

# Display list
obj.display()