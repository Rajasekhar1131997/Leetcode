# Leetcode Problem 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy Node for the result Linked List
        dummy = ListNode()
        # Point our current pointer to dummy node
        current = dummy
        # Initalizing the carry value to 0
        carry = 0
        # Looping until the l1 or l2 or carry has values
        while l1 or l2 or carry:
            # Get the l1 value to value1
            value1 = l1.val if l1 else 0
            # Get the l2 value to value2
            value2 = l2.val if l2 else 0
            
            # Calculate the total along with carry
            total = value1 + value2 + carry
            # We need to find the carry if our total exceeds 10 or more
            carry = total // 10
            # Create a ListNode with the current total value (total%10 gives the ones digit)
            current.next = ListNode(total % 10)
            # Move to the next pointer of our new linked list
            current = current.next

            # We move to the next value in l1 if exists
            if l1:
                l1 = l1.next
            # We move to the next value in l2 if exists
            if l2:
                l2 = l2.next
        # returning the final linked list
        return dummy.next
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")