# Leetcode Problem 617: Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if no first tree is provided, we simply return the second tree
        if not root1:
            return root2
        # if the second tree is not provided, we return the first tree
        if not root2:
            return root1
        # find the root node and create a TreeNode for the root
        root = TreeNode(root1.val + root2.val)
        # traverse the left subtrees by adding root1.left and root2.left
        root.left = self.mergeTrees(root1.left, root2.left)
        # traverse the right subtrees by adding root1.right and root2.right
        root.right = self.mergeTrees(root1.right, root2.right)
        # finally, return the root of the tree
        return root

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree")