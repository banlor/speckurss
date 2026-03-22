class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is not None:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        if n <= 0 or self.start is None:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        pos = 0
        while current.nref is not None and pos < n - 1:
            current = current.nref
            pos = pos + 1

        new_node.nref = current.nref
        new_node.pref = current
        if current.nref is not None:
            current.nref.pref = new_node
        else:
            self.end = new_node
        current.nref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.print()
q.insert(2, 99)
q.print()
print(q.pop())
q.print()
