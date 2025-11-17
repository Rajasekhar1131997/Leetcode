# Leetcode Problem 513: Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # convert the given tree into queue
        queue = deque([root])
        # loop until we process all the values from the queue
        while queue:
            # popoff the left most element from queue
            current = queue.popleft()
            # since, we need to get the leftmost element, we append the nodes from the right side of the tree to queue
            if current.right:
                queue.append(current.right)
            # add the left nodes to the queue
            if current.left:
                queue.append(current.left)
        # return the left most value in the last row of the tree
        return current.val

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")