# Leetcode Problem 876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# Definition for singly-linked list.
# Solving this problem using Slow-fast pointer technique
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initializing our slow and fast pointers pointing to head of the linked list
        slow = head
        fast = head
        # loop until we reach the last node of the linked list
        while fast and fast.next:
            # slow pointer moves one step each time
            slow = slow.next
            # fast pointer moves two steps each time
            fast = fast.next.next
        # return the slow pointer
        return slow
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")