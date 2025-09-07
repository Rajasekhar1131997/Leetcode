# Leetcode Problem 637: Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # initialize a queue with root node
        queue = deque([root])
        # initialize an empty result list to store average values
        result = []
        # while queue is not empty
        while queue:
            # find the length of the level
            level_length = len(queue)
            # initialize the sum to keep track of each level
            sum = 0
            # for every value in that level
            for i in range(level_length):
                # popleft the value
                node = queue.popleft()
                # add those values
                sum += node.val
                # find the average
                average = sum/level_length
                # if there are any left nodes available, add them to queue
                if node.left:
                    queue.append(node.left)
                # if there are any right nodes available, add them to queue
                if node.right:
                    queue.append(node.right)
            # finally, add the level average to result list
            result.append(average)
        # return the average result list
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")