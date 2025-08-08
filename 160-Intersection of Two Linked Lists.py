# Leetcode Problem 160: Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if no head node is given return None
        if not headA:
            return None
        if not headB:
            return None
        # point the headA to current_a pointer
        current_a = headA
        # point the headB to current_b pointer
        current_b = headB

        # Traverse until they meet or both reach None
        while current_a != current_b:
            # # Move to the next node or switch list
            current_a = current_a.next if current_a else headB
            current_b = current_b.next if current_b else headA
        return current_a

print("Time Complexity: O(M + N)")
print("Space Complexity: O(1)")