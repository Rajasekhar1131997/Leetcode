# Leetcode Problem 404: Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
# Solving this problem using BFS Approach
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # if no root is give, we return 0
        if not root:
            return 0
        # Initializing queue with the root node
        queue = deque([root])
        # initializing total value to 0
        total = 0
        # loop until we traverse all the nodes in tree
        while queue:
            # popleft the current node
            node = queue.popleft()

            # if there is a left node of the tree
            if node.left:
                # check if the left node is a leaf node or not
                if not node.left.left and not node.left.right:
                    # if it's a leaf node, add that value to result
                    total += node.left.val
                # else, we add that node to queue
                else:
                    queue.append(node.left)
            # also check if the tree has right nodes.
            if node.right:
                # append the right node to the queue
                queue.append(node.right)
        # return the total value
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(N) in worst case")