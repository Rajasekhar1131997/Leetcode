# Leetcode Problem 783: Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # initialize an empty output to store all the node values of tree
        output = []
        # convert the given tree into root
        queue = deque([root])
        # loop until we process all the nodes from queue
        while queue:
            # find the size of queue for each level
            size = len(queue)
            # loop until we process all the nodes in each level
            for _ in range(size):
                # pop off the value from the queue and add that value to output list
                node = queue.popleft()
                output.append(node.val)
                # if there are nodes to the left of the node, we append them to queue
                if node.left:
                    queue.append(node.left)
                # if there are any nodes to the right, we append them to queue
                if node.right:
                    queue.append(node.right)
        # sort the output list
        output.sort()
        # let the min value be infinity
        min_value = float('inf')
        # loop through output list and finding the min difference b/w node values
        for i in range(1, len(output)):
            difference = abs(output[i-1] - output[i])
            min_value = min(difference, min_value)
        # returning the min value among the whole tree nodes
        return min_value

print("Time Complexity: O(N log N) => logn is due to sorting")
print("Space Complexity: O(N)")