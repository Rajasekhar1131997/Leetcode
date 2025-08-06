# Leetcode Problem 21: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy Node
        dummy = ListNode()
        # Assign that dummy node to tail
        tail = dummy
        # When both the lists are non-empty
        while list1 and list2:
            # checking if the value in list1 is smaller than list2
            if list1.val < list2.val:
                # Attach that node to the tail
                tail.next = list1
                # move to the next value in the list
                list1 = list1.next
            # If the value in list2 is smaller than list1
            else:
                # Attach that node the tail
                tail.next = list2
                # Move to the next value in the list
                list2 = list2.next
            # Proceed to the next node
            tail = tail.next
        # If there are any values left in the list1, attach them at the end of the linked list
        if list1:
            tail.next = list1
        # If there are any values left in the list2, attach them at the end of the linked list
        elif list2:
            tail.next = list2
        # return the merged list
        return dummy.next

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")