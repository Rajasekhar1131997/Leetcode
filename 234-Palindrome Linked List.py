# Leetcode Problem 234: Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        # Initialize an empty list to add the values of all nodes to the list
        result = []
        # pointing head to current pointer
        current = head
        # loop until it reaches the end, and add all the values to result list
        while current:
            result.append(current.val)
            current = current.next
        # initialize left and right pointers on the list
        left, right = 0, len(result) - 1
        # loop until we process each value in list
        while left < right:
            # logic to check if the linked list is palindrome or not
            if result[left] == result[right]:
                # move left pointer to the right in list
                left += 1
                # move right pointer to the left in list
                right -= 1
            # if they are not equal, our list is not palindrome and we return false
            else:
                return False
        # we return true if the above case fails
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")