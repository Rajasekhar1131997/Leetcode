# Leetcode Problem 19: Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize the dummy Node with 0 and next pointer to head
        dummy = ListNode(0, head)
        # initialize the p1 pointer to head
        p1 = head
        # initialize the p2 pointer to dummy
        p2 = dummy
        # initialize the count to 0
        count = 0
        # Traversing the p1 pointer, if we keep increasing the p1 pointer, somewhere the p2 pointer will reach to the node before that we need to attach
        while p1 != None:
            p1 = p1.next
            count += 1
            # if the count is greater than n
            if count > n:
                # we move the p2 pointer
                p2 = p2.next
        # Point the next pointer next to next
        p2.next = p2.next.next
        # we return the next pointer of dummy node, which is head
        return dummy.next

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")