# Leetcode Problem 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# Solving this problem using Iterative Approach and Two Pointers
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the head or linked list is empty, we return None
        if not head:
            return None
        # Initialize the prev pointer to None
        prev = None
        # Initialize the current pointer to head of the linked list
        current = head
        # Loop until the list is not empty
        while current:
            # Initialize the temp pointer which holds the value of next pointer of current
            temp = current.next
            # We are doing the reversing here by pointing current.next to prev(which holds None)
            current.next = prev
            # We move forward and make the prev pointer to current
            prev = current
            # We also move to the next value in the list
            current = temp
        # we return the prev value which is the current head
        return prev

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")