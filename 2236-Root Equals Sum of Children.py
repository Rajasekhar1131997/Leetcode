# Leetcode Problem 2236: Root Equals Sum of Children
# https://leetcode.com/problems/root-equals-sum-of-children/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # we check if the root value is equal to the sum of its left and right child
        return root.val == root.left.val + root.right.val

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")