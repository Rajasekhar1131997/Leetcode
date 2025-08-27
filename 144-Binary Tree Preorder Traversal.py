# Leetcode Problem 144: Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing an empty result list to store the values
        result = []
        # using the helper function to traverse the tree in Preorder -> current, left, right
        def dfs(node):
            # if there is no node or empty, we exit or return from the helper function
            if not node:
                return
            # since, it is preorder, we add the root value first
            result.append(node.val)
            # traversing the left side of the tree
            dfs(node.left)
            # traversing the right side of the tree
            dfs(node.right)
        # calling the helper function with root node
        dfs(root)
        # return the result node values
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(H), H is tree height, O(N) in worstcase")