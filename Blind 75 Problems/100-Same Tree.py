# Leetcode Problem 100: Same Tree
# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Solving the Problem using Depth First Search Recursive Appriach
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both the binary trees are empty, we return True
        if not p and not q:
            return True
        # If any of the binary trees are empty, we return False
        if not p or not q:
            return False
        # if the binary tree's val are not equal, we return False
        if p.val != q.val:
            return False
        # Recursing the left subtree tree and right tree
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree," \
"O(log N) for the balanced binary tree," \
"O(N) in the worst case for skewed tree")

# Solving the problem using Breadth First Search Approach using queue
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize the queue with the root node of two trees
        queue = deque([(p,q)])
        # while the queue is not empty
        while queue:
            # pop off the tree root values
            node1, node2 = queue.popleft()
            # If both the roots of the trees are empty, we continue to next step
            if not node1 and not node2:
                continue
            # If either of the roots of the trees are empty, we return False
            if not node1 or not node2:
                return False
            # If the root values are not equal, we return False
            if node1.val != node2.val:
                return False
            # Append the left subtree values of both the trees to queue
            queue.append((node1.left, node2.left))
            # Append the right subtree values of both the trees to queue
            queue.append((node1.right, node2.right))
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")