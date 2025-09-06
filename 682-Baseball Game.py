# Leetcode Problem 682: Baseball Game
# https://leetcode.com/problems/baseball-game/description/
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # initialize an empty stack
        stack = []
        # loop through each string in operations
        for op in operations:
            # if op == "C", we have to pop the previous value
            if op == "C":
                stack.pop()
            # if the op is "D", we have to double the previous value and add it to stack
            elif op == "D":
                stack.append(stack[-1] * 2)
            # if the op is "+", we have to add the previous two values and add it to stack
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            # else, we continue adding the values to stack
            else:
                stack.append(int(op))
        # we return the sum of the values in stack list
        return sum(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")