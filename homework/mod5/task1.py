class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        items = []
        while current is not None:
            items.append(str(current.data))
            current = current.pref
        items.reverse()
        for item in items:
            print(item, end=" ")
        print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.print()
print(s.pop())
s.print()
