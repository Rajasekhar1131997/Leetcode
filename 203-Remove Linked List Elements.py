# Leetcode Problem 203: Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Initialize and temp node or dummy node with 0 and next pointer locating to head
        temp = ListNode(0, head)
        # make the current pointer pointing to temp node
        current = temp
        # loop until all the nodes are processed
        while current and current.next:
            # if the current pointer value is same as the given value, we need to skip it
            if current.next.val == val:
                # pointing the next pointer location to the upcoming pointer
                current.next = current.next.next
            # if the node value is not equal, we simply move to the next pointer
            else:
                current = current.next
        # return the next of the temp node, that's where our new head starts
        return temp.next
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")