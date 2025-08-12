# Leetcode Problem 110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # using helper function to depth first search the bottom-up approach
        def dfs(root):
            # if not root of the node, we return True and height as 0
            if not root: return [True, 0]
            # similarly, we check every left and right subtree nodes
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            # we find the difference between two trees and it should be <=1
            difference = abs(left_subtree[1] - right_subtree[1]) <=1
            # we need to make sure that the node is balanced checking from bottom
            balanced = (left_subtree[0] and right_subtree[0] and difference)

            # we return the Boolean value and height of the tree as the output
            return [balanced, 1 + max(left_subtree[1],right_subtree[1])]
        
        # we return the Boolean value as the output
        return dfs(root)[0]

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the tree height (recursion stack). It can be O(N) in worstcase if it's a skewed tree and O(log N) if balanced")