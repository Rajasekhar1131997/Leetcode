# Leetcode Problem 222: Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if there is no root, we return 0
        if not root:
            return 0
        # traverse the left subtree
        left_subtree = self.countNodes(root.left)
        # traverse the right subtree
        right_subtree = self.countNodes(root.right)
        
        # return sum of left subtree and right subtree plus 1, since we are starting from root node
        return 1 + left_subtree + right_subtree
    
print("Time Complexity: O(N)")
print("Space Complexity: O(H) and O(N) in worst case")