# Leetcode Problem 1302: Deepest Leaves Sum
# https://leetcode.com/problems/deepest-leaves-sum/description/
# solving this problem using BFS approach
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # if the root node is null, we exit the function
        if not root:
            return
        # converting the given root into queue
        queue = deque([root])
        # loop until there are no values in queue
        while queue:
            # let the level sum be 0 for every level
            level_sum = 0
            # loop until we process all the values in every level
            for i in range(len(queue)):
                # pop the nodes from left side
                node = queue.popleft()
                # compute the level sum for each level
                level_sum += node.val
                # if there are any node to left, we append them to queue
                if node.left:
                    queue.append(node.left)
                # if there are any nodes to right, we append them to queue
                if node.right:
                    queue.append(node.right)
        # since, we are calculating level_sum for each level, at the end, we have the sum of deepest leaves, so we return that value
        return level_sum

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")