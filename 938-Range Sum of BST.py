# Leetcode Problem 938: Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # call the helper function with root node, low and high values
        find_total = self.dfs(root, low, high)
        # return the total value returned by helper function
        return find_total
    
    # helper function to process the tree
    def dfs(self, node: Optional[TreeNode], low: int, high: int) -> int:
        # initialize the total to 0
        total = 0
        # if there is no root node, we return 0
        if not node:
            return 0
        # check if the node is in inclusive range and add it to total
        if node.val >= low and node.val <= high:
            total += node.val
        # call the left subtree
        total += self.dfs(node.left, low, high)
        # call the right subtree
        total += self.dfs(node.right,low, high)
        # return the total value
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree")