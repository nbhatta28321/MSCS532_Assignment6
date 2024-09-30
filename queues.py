class Queue:

    def __init__(self, size) -> None:
        self.queue = [0] * size
        self.size = size
        self.front = 0
        self.back = 0

    def enqueue(self, value): #add element from the back

        if self.back > self.size:
            print("Queue is full")
            return

        self.queue[self.back] = value
        self.back += 1

        print("After insertion in queue", self.queue)
        return
    
    def dequeue(self):

        if self.front >= self.back:
            print("Queue is empty")
            return
        
        self.queue[self.front] = 0

        for i in range(self.back):
            self.queue[i] = self.queue[i+1]

        self.back -=1    

        print("After dequeue", self.queue)

        return
    
    def search(self, value):

        if self.front >= self.back:
            print("Queue is empty")
            return
        
        j = self.front
        
        while j != self.back:
            if self.queue[j] == value:
                print(f"Found the value {value} at index {j}")
                return

            j +=1  

        print(f"Not found value {value}")      
        return

    
queue = Queue(10)

queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(3)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(3)

queue.search(3)
queue.search(6)
