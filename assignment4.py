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
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def Palindrome(self, string1):
        s = Stack()
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

    def evaluate_infix_expression(self, expression):
        def precedence(operator):
            if operator in '*/':
                return 2
            elif operator in '+-':
                return 1
            else:
                return 0

        def apply_operation(operators, numbers):
            operator = operators.pop()
            num2 = numbers.pop()
            num1 = numbers.pop()
            if operator == '+':
                numbers.push(num1 + num2)
            elif operator == '-':
                numbers.push(num1 - num2)
            elif operator == '*':
                numbers.push(num1 * num2)
            elif operator == '/':
                numbers.push(num1 / num2)

        numbers_stack = Stack()
        operators_stack = Stack()

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                numbers_stack.push(num)
                i -= 1
            elif expression[i] == '(':
                operators_stack.push(expression[i])
            elif expression[i] == ')':
                while operators_stack.peek() != '(':
                    apply_operation(operators_stack, numbers_stack)
                operators_stack.pop()
            elif expression[i] in '+-*/':
                while not operators_stack.is_empty() and precedence(expression[i]) <= precedence(operators_stack.peek()):
                    apply_operation(operators_stack, numbers_stack)
                operators_stack.push(expression[i])
            i += 1

        while not operators_stack.is_empty():
            apply_operation(operators_stack, numbers_stack)

        return numbers_stack.pop()

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
        #am really sorry but this code is not working as intended and i don't know how to fix it
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
class Graph:
    def __init__(self,num_vertices):
        self.num_vertices=num_vertices
        self.adj_matrix=[[0]*num_vertices for _ in range(num_vertices)]
    def addVertex(self):
        self.num_vertices+=1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0]*self.num_vertices)
    def addEdge(self,v1,v2):
        if 0<=v1< self.num_vertices and 0<=v2< self.num_vertices:
            self.adj_matrix[v1][v2]=1
            self.adj_matrix[v2][v1]=1
        elif (v1<0 or v1>=self.num_vertices)and (v2<0 or v2>=self.num_vertices):
            print('Invalid vertices')
        elif v1<0 or v1>=self.num_vertices:
            print('vertex',v1," is invalid")
        else:
            print('vertex',v2," is invalid")

    def remove_vertex(self, v):
        if 0 <= v < self.num_vertices:
            del self.adj_matrix[v]
            for row in self.adj_matrix:
                del row[v]
            self.num_vertices -= 1
    def remove_edge(self,v1,v2):
        if 0<=v1< self.num_vertices and 0<=v2< self.num_vertices:
            self.adj_matrix[v1][v2]=0
            self.adj_matrix[v2][v1]=0
        elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
            print('Invalid vertices')
        elif v1 < 0 or v1 >= self.num_vertices:
            print('vertex', v1, " is invalid")
        else:
            print('vertex', v2, " is invalid")
    def count_degrees(self,n):
        degrees = [0] * self.num_vertices
        vertices_to_display = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] == 1:
                    degrees[i] += 1
        for i in range(len(degrees)):
            if degrees[i] >= n:
                vertices_to_display.append(i)
        print(f"Vertices with degree >= {n}:")
        for vertex in vertices_to_display:
            print(vertex)


def main():
    ll = LinkedList()
    stack=Stack()
    queue=PriorityQueue()
    graph=Graph(0)
    counter=0
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
        elif choice == '4':
            expression = input("Enter the infix expression: ")
            print(stack.evaluate_infix_expression(expression))
        elif choice == '5':
            print('a. Add vertex')
            print('b. Add edge')
            print('c. Remove vertex')
            print('d. Remove edge')
            print('e. Display vertices with a degree of X or more.')
            print('f. Return to main menu')
            option = input('please choose ')
            if option == 'a':
                graph.addVertex()
            elif option == 'b':
                v1=int(input('please enter the first vertex '))
                v2=int(input('please enter the second vertex '))
                graph.addEdge(v1,v2)
            elif option == 'c':
                v=input('please enter the vertex you want to remove ')
                graph.remove_vertex(v)
            elif option == 'd':
                v1=int(input('please enter the first vertex '))
                v2=int(input('please enter the first vertex '))
                graph.remove_edge(v1,v2)
            elif option == 'e':
                degree=int(input('please enter the degree of the vertices you want to display '))
                graph.count_degrees(degree)
            elif option == 'f':
                continue
        elif choice == '6':
            print('Have a Good Day')
            break
        else:
            counter+=1
            if counter<4:
                print('please choose only from the given choices')
            else:
                break
main()