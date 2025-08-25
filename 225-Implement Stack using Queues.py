# Leetcode Problem 225: Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/
class MyStack:

    # definition of stack
    def __init__(self):
        self.stack = []
    
    # using append operation we push the values to stack
    def push(self, x: int) -> None:
        self.stack.append(x)

    # using pop operation, we pop the value from the stack
    def pop(self) -> int:
        return self.stack.pop()

    # returning the top of the stack using stack[-1]
    def top(self) -> int:
        return self.stack[-1]

    # we check the length of stack, if it's 0, we return True else False
    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

print("Time Complexity: O(1), all the operations in stack takes O(1) time")
print("Space COmplexity: O(N)")