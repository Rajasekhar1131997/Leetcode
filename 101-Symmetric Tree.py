# Leetcode Problem 101: Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Using DFS recursive approach to solve this problem
        # Creating an recursive helper function mirror with left and right nodes
        def mirror(a:Optional[TreeNode], b:Optional[TreeNode]) -> bool:
            # if there is no left and right childs, we return true
            if not a and not b:
                return True
            # if there is no left or right child or if their values are not equal, we return False
            if not a or not b or a.val != b.val:
                return False
            # Traversing through the tree
            return mirror(a.left, b.right) and mirror(a.right, b.left)
        # return True if there is no root else we traverse left and right trees
        return True if not root else mirror(root.left, root.right)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(H) where H is the height of the tree and O(N) in worst case")