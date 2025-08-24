# Leetcode Problem 83: Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assigning the head to current
        current = head
        # loop until we process we reach end of the linked list, we need to check until both current and current.next exists
        while current and current.next:
            # check if the current and next pointer holds the same value or not
            if current.val == current.next.val:
                # if it holds, we update the next pointer of current to current.next.next
                current.next = current.next.next
            # else, we simply move forward out pointer
            else:
                current = current.next
        # we need to return the head of the linked list
        return head

print("TIme Complexity: O(N)")
print("Space Complexity: O(1)")