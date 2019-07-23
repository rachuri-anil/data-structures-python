class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SlinkedList:
    '''
        Create a link list
    '''

    def __init__(self):
        self.head = None

    def print_list(self):
        '''
        Traverse through the linked list
        Returns: None
        '''
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def insert_at_beginning(self, new_data):
        '''
        Insets an new node at the beginning
        Args:
            new_data:

        Returns: None
        '''
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_data):
        '''

        Args:
            new_data:

        Returns:

        '''
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_in_between(self, middle_node, new_data):
        '''
        Inserts a new node after a given node
        Args:
            middle_node:
            new_data:

        Returns:

        '''
        if middle_node is None:
            print("Middle Node absent")
            return
        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node


if __name__ == "__main__":
    week_list = SlinkedList()
    week_list.head = Node("Monday")
    second_node = Node("Tuesday")
    third_node = Node("Wednesday")
    week_list.head.next = second_node
    second_node.next = third_node
    print("Traversing a list ")
    week_list.print_list()
    # inserting ant beginning
    week_list.insert_at_beginning("Sunday")
    print("Inserting a new node at beginning(Sunday)")
    week_list.print_list()
    week_list.insert_at_end("Thursday")
    print("Inserting the new node at last")
    week_list.print_list()
    week_list.insert_in_between(second_node, "random_value")
    print("After a random insert")
    week_list.print_list()
