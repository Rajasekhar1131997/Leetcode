# Leetcode Problem 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# Solving the problem using Depth First Search Approach and Recursion
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, we return 0
        if not root:
            return 0
        # Traversing the left_subtree
        left_subtree = self.maxDepth(root.left)
        # Traversing the right_subtree
        right_subtree = self.maxDepth(root.right)
        # finding the maximum value of both subtrees and adding 1(because of root)
        return max(left_subtree, right_subtree) + 1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# Definition for a binary tree node.
# Solving the problem using Breadth First Search Approach using Queue.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if the tree is empty, return 0
        if not root:
            return 0
        # Initialize the queue with root node
        queue = deque([root])
        # Initialize variable to keeo track of the maximum depth
        count = 0
        # loop until the queue is not empty
        while queue:
            # find the length of each level
            level_length = len(queue)
            # pop off each element from the queue
            for i in range(level_length):
                node = queue.popleft()
                # if left child is available, append that node to the queue
                if node.left:
                    queue.append(node.left)
                # if the right child is available, append that node to the queue
                if node.right:
                    queue.append(node.right)
            # Increment the count for each level
            count += 1
        # return the final depth
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")