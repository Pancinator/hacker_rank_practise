class MyQueue():
    my_list = []

    def enque(self, num):
        self.my_list.append(num)

    def deque(self):
        self.my_list.pop(0)

    def peek(self):
        return self.my_list[0]

if __name__ == '__main__':
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        if values[0] == 1:
            queue.enque(values[1])
        elif values[0] == 2:
            queue.deque()
        else:
            print(queue.peek())