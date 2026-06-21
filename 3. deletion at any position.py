# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end (creation)
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Delete at head
    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    # Delete at any position (0-based indexing)
    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 0:
            self.head = self.head.next
            return

        current = self.head

        # Move to node just before the position
        for _ in range(pos - 1):
            if current is None or current.next is None:
                print("Invalid position")
                return
            current = current.next

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

    # Display linked list
    def display(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Driver Code
ll = LinkedList()

# Creation
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

print("Original List:")
ll.display()

# Delete head
ll.delete_head()
print("After deleting head:")
ll.display()

# Delete end
ll.delete_end()
print("After deleting end:")
ll.display()

# Delete node at index 1 (0-based)
ll.delete_position(1)
print("After deleting index 1:")
ll.display()
