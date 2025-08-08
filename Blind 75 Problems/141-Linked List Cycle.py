# Leetcode Problem 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# Solving this problem using Slow-Fast Pointer technique
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if there is no head of the linked list, we return None
        if not head:
            return None
        # initializing the pointers slow and fast and pointing them to head
        slow = head
        fast = head
        # looping until the fast pointer reaches the end of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if the slow pointer meets the fast pointer, i.e., if follows a loop and we return True
            if slow == fast:
                return True
        # if there is no loop, we return false
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")