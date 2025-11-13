# Leetcode Problem 237: Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # since we don't need to return the head node, we assign the next node value to given node
        node.val = node.next.val
        # we also point the current node next pointer to next node next pointer
        node.next = node.next.next

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")