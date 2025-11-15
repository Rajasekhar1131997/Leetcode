# Solving this problem using recursive approach
# Leetcode Problem 2181: Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the next node of head is null, we return None
        if not head.next:
            return None
        # assing the next pointer of head to current
        current = head.next
        # let the sum be 0
        summ = 0
        # loop until we find the next value is 0
        while current.val != 0:
            # compute the sum until the next consecutive 0
            summ += current.val
            # increment the pointer
            current = current.next
        
        # assign the sum to next pointer of head
        head.next.val = summ
        # we call the function again with the next head
        head.next.next = self.mergeNodes(current)
        # we return the new head after merging all the nodes lying in b/w 0's
        return head.next

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")