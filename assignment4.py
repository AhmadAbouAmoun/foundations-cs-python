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
        while current and current.data==info:
            self.head=current.next
            current=self.head
        prev_node=None
        while current :
            if current.data==info:
                prev_node.next=current.next
                current=current.next
            else:
                prev_node=current
                current=current.next

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def isEmpty(self):
        return self.head==None
    def push(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
        self.size+=1
    def pop(self):
        if self.size==0:
            print("nothing")
        else:
            current=self.head
            self.head=self.head.next
            current.next=None
            self.size-=1
    def peek(self):
        if self.size==0
            print('nothing')
        else
            return self.head.data



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
            elif option == 'b':
                ll.print_list()
            elif option == 'c':
                info=input("please enter the value that you want to delete ")
                ll.delete_node(info)
            elif option == "d":
                continue
        elif choice == '2':


main()