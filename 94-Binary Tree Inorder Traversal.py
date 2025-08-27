# Leetcode Problem 94: Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing an empty list to store the values
        result = []
        # using the helper function to traverse the tree inorder -> left, root, right
        def dfs(node):
            # if the node is null or no root, we return or exit
            if not node:
                return
            # traversing the tree left side
            dfs(node.left)
            # adding the root value to the result list
            result.append(node.val)
            # traversing the tree right side
            dfs(node.right)
        # calling the helper function with root of the tree
        dfs(root)
        # returning the result
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(H), H is tree height, O(N) in worstcase")