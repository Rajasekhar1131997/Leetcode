# Leetcode Problem 1441: Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/description/
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # initialize an empty stack to store the stack actions
        stack = []
        # let the current variable be 1
        current = 1
        # loop through the values in target
        for i in target:
            # if current value is less than i, we keep pushing push and pop to stack
            while current < i:
                stack += ["Push", "Pop"]
                # we also keep incrementing the current by 1
                current += 1
            # we append push action to stack
            stack.append("Push")
            # we also increment current by 1
            current += 1
        # return the stack with operations at the end
        return stack
        
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")