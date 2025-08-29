# Leetcode Problem 112: Path Sum
# https://leetcode.com/problems/path-sum/description/
# Solving this problem using DFS Approach
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if the root node is empty or no root, we return False
        if not root:
            return False
        # if there is a leaf node and targetsum is equal to that leaf node, we return True or False
        if not root.left and not root.right:
            return root.val == targetSum
        # for every node, we calculate the remaining sum
        rem = targetSum - root.val
        # we traverse through the left and right subtree at each node while keeping track of remaining sum
        return self.hasPathSum(root.left, rem) or self.hasPathSum(root.right, rem)

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree, O(N) in worst case")