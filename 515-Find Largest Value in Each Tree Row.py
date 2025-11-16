# Leetcode Problem 515: Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if the given tree is empty or root node is None, we return []
        if not root or root is None:
            return []
        # convert the given tree into queue
        queue = deque([root])
        # initialize an empty output list to hold the result
        output = []
        # loop until we process all the nodes in tree
        while queue:
            # let the max value be negative infinity
            max_value = float('-inf')
            # find the length of each level
            size = len(queue)
            # loop until we process all the nodes in each level
            for i in range(size):
                node = queue.popleft()
                # check if the recently popped value is greater than previous popped value
                if node.val > max_value:
                    max_value = node.val
                # append the left node values to queue
                if node.left:
                    queue.append(node.left)
                # append the right node values to queue
                if node.right:
                    queue.append(node.right)
            # append that max value of each row to output
            output.append(max_value)
        # finally, return the output value
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")