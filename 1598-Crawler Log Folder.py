# Leetcode Problem 1598: Crawler Log Folder
# https://leetcode.com/problems/crawler-log-folder/
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # initialize an empty stack to store the words
        stack = []
        # loop through each word in logs
        for word in logs:
            # if the stack is not empty and word is ../, we pop the previous value from stack
            if word == "../":
                if stack:
                    stack.pop()
            # if the word is ./, we ignore the word and continue with next word
            elif word == "./":
                continue
            # else, we append that word to stack
            else:
                stack.append(word)
        # returning the length of stack denotes no.of operations needed to go back to main folder
        return len(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")