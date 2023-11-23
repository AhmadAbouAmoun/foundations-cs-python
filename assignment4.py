class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    def delete_node(self,info):
        current=self.head
        while current:
            if current.data==info:


def main():
    ll = LinkedList()
    while True:
        print('1. Singly Linked List')
        print('2. Check if Palindrome')
        print('3. Priority Queue')
        print('4. Evaluate an Infix Expression')
        print('5. Graph')
        print('6. Exit')
        choice = input('choose what you want ')

        if choice == '1':
            print('a. Add Node')
            print('b. Display Nodes')
            print('c. Search for & Delete Node')
            print('d. Return to main menu')
            option = input('please choose ')
            if option == 'a':
                data = input("please enter data ")
                ll.append(data)
            if option == 'b':
                ll.print_list()


main()