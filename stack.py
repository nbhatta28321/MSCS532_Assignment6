class Stack:

    def __init__(self, size) -> None:
        self.stack = [0] * size
        self.size = size
        self.numOfelements = 0

    def push(self, value):

        if self.numOfelements > self.size:
            print("Stack is full")
            return

        self.stack[self.numOfelements] = value
        self.numOfelements += 1

        print("After insertion", self.stack)
        return
    
    def pop(self):

        if self.numOfelements <= 0:
            print("Stack is empty")
            return
        
        self.stack[self.numOfelements -1] = 0
        self.numOfelements -= 1

        print("After pop", self.stack)

        return
    
    def search(self, value):

        i = self.numOfelements
        while i > 1:
            if self.stack[i] == value:
                print(f"Found the value {value} at index {i}")
                return
            i-=1

        return
    
stack = Stack(10)

stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()
stack.pop()
stack.push(9)
stack.push(3)
stack.push(4)

stack.search(3)