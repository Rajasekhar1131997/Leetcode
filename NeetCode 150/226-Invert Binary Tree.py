# Leetcode Problem 226: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# Using BFS Approach to solve this problem
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the tree is empty, there is nothing to revert and somply return the root value
        if not root:
            return root
        # using BFS, so we use queue to check each level
        queue = deque([root])
        # loop until the queue is empty
        while queue:
            # popping off each value from the queue
            node = queue.popleft()
            # swapping the children in-place
            node.left, node.right = node.right, node.left

            # push the children if exists to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # return the root node after inverting the tree
        return root
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")