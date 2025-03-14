import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
        heapq.heapify(self.pq)
    
    def push(self, data):
        heapq.heappush(self.pq, -data)

    def pop(self):
        if not self.empty():
            return -heapq.heappop(self.pq)
    
    def size(self):
        return len(self.pq)

    def empty(self):
        return 0 if self.pq else 1
        
    def top(self):
        if not self.empty():
            return -self.pq[0]
        

N = int(input())

pq = PriorityQueue()

for n in range(N):
    op = input().split()
    if len(op) > 1:
        op, data = op[0], int(op[1])
        if op == "push":
            pq.push(data)
    else:
        op = op[0]
        if op == "size":
            print(pq.size())
        elif op == "pop":
            print(pq.pop())
        elif op == "top":
            print(pq.top())
        elif op == "empty":
            print(pq.empty())
        



