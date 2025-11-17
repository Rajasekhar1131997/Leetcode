# Leetcode Problem 1609: Even Odd Tree
# https://leetcode.com/problems/even-odd-tree/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # if the tree is empty or no root is given, we return False
        if not root or root is None:
            return False
        # convert the given tree into queue
        queue = deque([root])
        # let the level be 0
        level = 0
        # loop until we process all the nodes in the tree
        while queue:
            # initialize an empty level list
            level_list = []
            # find the size of the each level from queue
            size = len(queue)
            # loop until we process all the nodes at each level
            for i in range(size):
                node = queue.popleft()
                level_list.append(node.val)

                # add left nodes to the queue
                if node.left:
                    queue.append(node.left)
                # add right nodes to the queue
                if node.right:
                    queue.append(node.right)
            # if the level is even, we need to check if all the values in the list are odd integer values or not and also need to make sure they are strictly increasing from left to right
            if level % 2 == 0:
                if any(val % 2 == 0 for val in level_list):
                    return False
                for i in range(len(level_list) - 1):
                    if level_list[i] >= level_list[i+1]:
                        return False
            # if the level is odd, we need to check if all the values in the list are even integer values or not and also need to make sure they are strictly decreasing from left to right
            else:
                if any(val % 2 == 1 for val in level_list):
                    return False
                for i in range(len(level_list) - 1):
                    if level_list[i] <= level_list[i+1]:
                        return False
            # increase the level by 1
            level += 1
        # return True
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")