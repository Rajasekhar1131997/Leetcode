# Leetcode Problem 145: Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing an empty result list to store node values
        result = []
        # using the helper function to traverse the tree in postorder -> left, right, current
        def dfs(node):
            # if there is no node or empty, we return or exit the helper function
            if not node:
                return
            # traversing the left subtree
            dfs(node.left)
            # traversing the right subtree
            dfs(node.right)
            # adding the current node value to result list
            result.append(node.val)
        # calling the helper function with root value
        dfs(root)
        # return the result list containing postorder traversal values
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(H) where H is the height of the tree, O(N) in worst case")