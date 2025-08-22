# Leetcode Problem 543: Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initiliaze a variable diameter with 0
        self.diameter = 0
        # Using Depth First Search approach to traverse the tree
        def dfs(node):
            # If there is no node, we return 0
            if not node:
                return 0
            # traverse the left subtree
            left = dfs(node.left)
            # traverse the right subtree
            right = dfs(node.right)
            # Finding the diameter
            self.diameter = max(self.diameter, left+right)
            return max(left, right) + 1
        # traverse from the root node
        dfs(root)
        # return the diameter
        return self.diameter

print("Time Complexity: O(N)")
print("Space Complexity: O(N) for worst case and O(log N) for Balanced Tree")