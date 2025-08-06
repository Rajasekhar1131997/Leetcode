# Leetcode Problem 111: Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# Solving the problem using Breadth First Search
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((root.left, depth+1))
            if node.right:
                queue.append((root.right, depth+1))

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# Solving the problem using Depth First Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, we simply return 0
        if not root:
            return 0
        # Initializing min_depth to infinity value
        self.min_depth = float('inf')
        # calling the dfs function with root node and depth of 1(since starting with node)
        self.dfs(root, 1)
        # return thr final min_depth value
        return self.min_depth
    
    def dfs(self, node, current_depth):
        # if the tree is empty, exit the function
        if not node:
            return
        # if the current node has no left and right children, find the min_depth
        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, current_depth)
        # traverse through the left_subtree
        self.dfs(node.left, current_depth + 1)
        # traverse through the right subtree
        self.dfs(node.right, current_depth + 1)

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree, and it's O(N) in the worst case for a skewed tree")