class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
        
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def pop_front(self):
        if self.head == None:
            return 
        # Node가 하나일때를 생각안함
        if self.size == 1:
            print(self.head.data)
            self.head = None
            self.tail = None
            self.size -= 1
            return 
        ret_value = self.head.data
        self.head = self.head.next
        self.prev = None
        self.size -= 1

        print(ret_value)

    def pop_back(self):
        if self.head == None:
            return 
        # Node가 하나일때를 생각안함
        if self.size == 1:
            print(self.tail.data)
            self.head = None
            self.tail = None
            self.size -= 1
            return 
        ret_value = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

        print(ret_value)
        
    def get_size(self):
        print(self.size)

    def empty(self):
        if self.head == None:
            print(1)
        else:
            print(0)
        

    def front(self):
        if self.head:
            print(self.head.data)

    def back(self):
        if self.head:
            print(self.tail.data)


N = int(input())

dl = doubly_linked_list()

for i in range(N):
    input_string = input().split()
    if len(input_string) == 1:
        op = input_string[0]
    else:
        op, num = input_string

    if op == 'push_front':
        dl.push_front(num)
    if op == 'push_back':
        dl.push_back(num)
    if op == 'pop_front':
        dl.pop_front()
    if op == 'pop_back':
        dl.pop_back()
    if op == 'size':
        dl.get_size()
    if op == 'empty':
        dl.empty()
    if op == 'front':
        dl.front()
    if op == 'back':
        dl.back()


