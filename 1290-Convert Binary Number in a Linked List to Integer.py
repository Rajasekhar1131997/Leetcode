# Leetcode Problem 1290: Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # initialize an empty string to store the binary string
        string = ""
        # list to store the each node value
        result = []
        # assigning head to current pointer
        current = head
        # loop until all the nodes in linked list are processed
        while current:
            # appending the current node value to result list
            result.append(current.val)
            # moving the current pointer to next node
            current = current.next
        # converting the result list to string
        string = "".join(str(num) for num in result)
        # using python inbuilt function int to convert the binary string to decimal value
        decimal_value = int(string, 2)
        # returning the decimal value
        return decimal_value

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")