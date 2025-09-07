# Leetcode Problem 965: Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # initialize an empty set
        values = set()
        # using depth first search helper function
        def dfs(node):
            # if there is no node, we return of exit the function
            if not node:
                return
            # traverse the left subtree
            dfs(node.left)
            # add each node value to set
            values.add(node.val)
            # traverse the right subtree
            dfs(node.right)
        # calling the helper function with root node
        dfs(root)
        # if the node values are different, we would have different values in set
        return len(values) == 1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")