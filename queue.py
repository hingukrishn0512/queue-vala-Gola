class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # Add at the end

    def dequeue(self):
        if not self.isempty():
            return self.queue.pop(0)  # Remove from front
        return "Queue is empty!"

    def peek(self):
        if not self.isempty():
            return self.queue[0]  # See the front item
        return "Queue is empty!"

    def isempty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)

# Example usage
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.display()              # Output: [5, 10, 15]

print("Front element:", q.peek())   # Output: 5
q.dequeue()
q.display()              # Output: [10, 15]
