# import sys
# def doSomething(inval):
#     #Do Something
#     return outval
# inputVal = input()    
# outputVal = doSomething(input)
# print (output)
                                                                                                                            

class CustomQueue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, element):
        self.stack_enqueue.append(element)

    def dequeue(self):
        if not self.stack_dequeue:
            # If the dequeue stack is empty, transfer elements from the enqueue stack
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            return None

    def front(self):
        if not self.stack_dequeue:
            # If the dequeue stack is empty, transfer elements from the enqueue stack
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue[-1]
        else:
            return None

# Function to process queries
def process_queries(query_str):
    custom_queue = CustomQueue()
    results = []

    queries = query_str.split(',')
    for query in queries:
        query_type, *args = map(int, query.split())
        
        if query_type == 1:
            # Enqueue
            custom_queue.enqueue(args[0])
        elif query_type == 2:
            # Dequeue
            custom_queue.dequeue()
        elif query_type == 3:
            # Print Front
            front_element = custom_queue.front()
            results.append(front_element)

    return results

# Take user input
user_input = input()
output_results = process_queries(user_input)

# Print the final result
for result in output_results:
    print(result)