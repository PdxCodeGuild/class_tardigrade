class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

# Alternatively, you can just implement a stack using a list and only appending to and popping from it.

stack = []
stack.append(1)
print(stack)  # > [1]
stack.append(2)
print(stack)  # > [1,2]
stack.append(3)
print(stack)  # > [1,2,3]
stack.pop()
print(stack)  # > [1,2]
stack.pop()   
print(stack)  # > [1]