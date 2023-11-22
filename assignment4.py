class node():
   def __init__(self,data):
       self.data = data
       self.next = None
class linkedList():
    def __init__(self):
        self.head = None

    def add_node(self):
        data = input('please enter the data of the linked list')
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            print('first node')
        else:
            new_node.next=self.head
            self.head=new_node
            print('it has been updated')

    def display_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    while True:
        print('1. Singly Linked List')
        print('2. Check if Palindrome')
        print('3. Priority Queue')
        print('4. Evaluate an Infix Expression')
        print('5. Graph')
        print('6. Exit')
        choice = input('choose what you want ')
        ll = linkedList()
        if choice == '1':
            print('a. Add Node')
            print('b. Display Nodes')
            print('c. Search for & Delete Node')
            print('d. Return to main menu')
            option = input('please choose ')
            if option == 'a':
                ll.add_node()
            if option == 'b':
                ll.display_linked_list()


main()