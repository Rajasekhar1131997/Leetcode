# Leetcode Problem 232: Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/
# import queue data structure from collections
from collections import deque
class MyQueue:
    
    # definition of queue
    def __init__(self):
        self.queue = deque()
    
    # using append operation, we add/push new value to queue
    def push(self, x: int) -> None:
        self.queue.append(x)

    # using popleft operation, we remove the front value from the queue and pop removes the latest value from queue
    def pop(self) -> int:
        return self.queue.popleft()

    # to check the first element enetered into the queue, we use queue[0]
    def peek(self) -> int:
        return self.queue[0]

    # we check the length of queue, if length is 0, we return True else False
    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

print("Time Complexity: O(1), all the operations takes O(1) time")
print("Space Complexity: O(N),, to store all the values in queues")