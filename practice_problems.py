"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""
#The data structure chosen for this task was a set because it only stores unique values, which makes it easier to identify duplicate values in the list.
#The has_duplicates function takes product_ids as an argument, converts the list to a set, and compares the length of each data structure
#to determine if duplicates are present, and returns a Boolean value of True or False. 
#The expected runtime for this operation is expected to increase with the number of product IDs because the function has to process the list to create the set.
def has_duplicates(product_ids):
    return len(product_ids) != len(set(product_ids))
print(has_duplicates([10, 20, 30, 20, 40]))


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
#The data structure that was chosen for this task was a Queue that was implemented with a Linked List because it follows the First in, First Out model, making it suitable for adding tasks to the back and removing tasks from the front of the queue.
#The Node and TaskQueue classes use next, front, and rear pointers to keep track of the nodes as tasks are added and removed.
#The runtime for adding and removing tasks are expected to stay remain the same as the queue grows because the front and rear nodes can be accessed directly.
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_oldest_task(self):
        if self.front is None:
            return None
        oldest_task = self.front.task
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return oldest_task

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code Review")
print(task_queue.remove_oldest_task())

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""
#The data structure chosen for this task was a set because it doesn't store duplicates, which makes it easy to determine the number of unique values.
#The UniqueTracker class initializes an empty set, uses add() to add values, and uses len() to return the number of unique values.
#The amount of time adding values and retrieving the word count takes are expected to remain constant even as the set grows.
class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())