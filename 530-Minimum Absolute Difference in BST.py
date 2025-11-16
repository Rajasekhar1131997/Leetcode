# Leetcode Problem 530: Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Solving this problem using Inorder DFS Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # let the previous node be None and min difference be infinity
        self.prev = None
        self.minDiff = float('inf')

        # traversing the tree using inorder helper function
        def inorder(node):
            # if there is no node, we return or exit the function
            if not node:
                return
            
            # traverse the left nodes of the tree
            inorder(node.left)
            
            # if the previous node is not none, we compute the min difference
            if self.prev is not None:
                self.minDiff = min(self.minDiff, node.val - self.prev)
            
            # we also update the previous node with current traversed node val
            self.prev = node.val

            # we also traverse the right nodes of the tree
            inorder(node.right)
        # calling the inorder function using the root of the tree
        inorder(root)
        # finally, we return the min difference
        return self.minDiff

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")