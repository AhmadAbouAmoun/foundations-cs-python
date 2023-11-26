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
        if self.size==0:
            print('nothing')
        else:
            return self.head.data
    def Palindrome(self,string1):
        s=Stack()
        for i in range(len(string1)):
            self.push(string1[i])
        reversed_string = ""
        for j in range(len(string1)):
            reversed_string += self.peek()
            self.pop()

        if string1 == reversed_string:
            print(string1, ' is palindromic')
        else:
            print(string1, ' is not palindromic')

class Student:
    def __init__(self,midterm_grade,final_grade,good_attitude):
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.head==None
    def enqueue(self,midterm,final,attitude):
        node=Student(midterm,final,attitude)
        if self.size == 0:
            self.head = node
            self.size += 1
        else:
            if node.good_attitude == True and self.head == False:
                node.next = self.head
                self.head = node
                self.size += 1
            elif node.good_attitude == True and self.head == True:
                if node.final_grade > self.head.final_grade:
                    node.next = self.head
                    self.head = node
                    self.size += 1
                elif node.final_grade == self.head.final_grade:
                    if node.midterm_grade >= self.head.midterm_grade:
                        node.next = self.head
                        self.head = node
                        self.size += 1
                    else:
                        current = self.head
                        previous = current
                        while current and current.good_attitude == True and node.final_grade <= current.final_grade and node.midterm_grade <= current.midterm_grade:
                            previous = current
                            current = current.next
                        if current.good_attitude != True or current.final_grade < node.final_grade or current.midterm_grade < node.midterm_grade:
                            previous.next = node
                            node.next = current
                            self.size += 1
                        else:
                            current.next = node
                            node.next = None
                else:
                    current = self.head
                    previous = current
                    while current and current.good_attitude == True and current.final_grade > node.final_grade:
                        previous = current
                        current = current.next
                        if current.final_grade == node.final_grade:
                            if current.midterm_grade <=node.midterm_grade:
                                previous.next = node
                                node.next = current
                                break
                        if current.good_attitude != True and current.final_grade < node.final_grade:
                            previous.next = node
                            node.next = current
                        else:
                            current.next = node
                            node.next = None
                    self.size += 1
            elif node.good_attitude == False and self.head == True:
                current = self.head
                previous = current
                while current and current.good_attitude == True:
                    previous = current
                    current = current.next
                if current.good_attitude != True:
                    if node.final_grade > current.final_grade:
                        previous.next = node
                        node.next = current
                        self.size += 1
                    elif node.final_grade == current.final_grade:
                        if node.midterm_grade >= current.midterm_grade:
                            previous.next = node
                            node.next = current
                            self.size += 1
                        else:
                            current.next = node
                            node.next = None
            elif node.good_attitude == False and self.head == False:
                if node.final_grade > self.head.final_grade:
                    node.next = self.head
                    self.head = node
                    self.size += 1
                elif node.final_grade == self.head.final_grade:
                    if node.midterm_grade >= self.head.midterm_grade:
                        node.next = self.head
                        self.head = node
                        self.size += 1
                    else:
                        current = self.head
                        previous = current
                        while current and current.final_grade > node.final_grade :
                            previous=current
                            current=current.next
                            if current.final_grade == node.final_grade:
                                if node.midterm_grade >= self.head.midterm_grade:
                                    node.next = current
                                    current = node
                                    self.size += 1
                                    break
                        if current.final_grade < node.final_grade:
                            node.next = current
                            current = node
                            self.size +=1
    def dequeue(self):
        if self.size == 0:
            print('it is already empty')
        elif self.size == 1:
            print(self.head.final_grade," ",self.head.good_attitude," ",self.head.midterm_grade)
            self.head = None
            self.size -= 1

        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
            print(current.good_attitude, " ", current.final_grade, " ", current.midterm_grade)


def main():
    ll = LinkedList()
    stack=Stack()
    queue=PriorityQueue()
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
                info = input("please enter the value that you want to delete ")
                ll.delete_node(info)
            elif option == "d":
                continue
        elif choice == '2':
            string1 = input("please enter the first string ")
            stack.Palindrome(string1)
        elif choice == '3':
            print('a. Add a student to the queue')
            print('b. Interview a student')
            print('c. Return to main menu')
            option = input('please choose ')
            if option == 'a':
                good_attitude=input('please enter the attitude of the student you want to add to the waiting list ')
                final_grade = input('please enter the final grade of the student you want to add to the waiting list ')
                midterm_grade = input('please enter the midterm grade of the student you want to add to the waiting list ')
                queue.enqueue(midterm_grade,good_attitude,final_grade)
            elif option == 'b':
                queue.dequeue()
            elif option == 'c':
                continue


main()