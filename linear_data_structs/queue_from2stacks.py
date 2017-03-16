class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def dequeue_fromcourse(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

if __name__ == '__main__':

    q = Queue2Stacks()

    for i in range(5):
        q.enqueue(i)

    for _ in range(5):
        print(q.dequeue())