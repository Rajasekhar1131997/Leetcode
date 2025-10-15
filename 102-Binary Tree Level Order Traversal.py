# Leetcode Problem 102: Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if the given root is empty, we return empty list
        if root is None:
            return []
        # initialize the empty list to add the level order list
        result = []
        # initialize the queue with root node
        queue = deque([root])
        # loop until each value in the queue is processed
        while queue:
            # initialize the level list to add values to the list at each level
            level_list = []
            # get the length of each level
            level_length = len(queue)
            # loop through each value in level length
            for i in range(level_length):
                # pop that value and append that value to level list
                node = queue.popleft()
                level_list.append(node.val)
                # if there are any left children to that node, append them to the queue
                if node.left:
                    queue.append(node.left)
                # if there are any right children to that node, append them to the queue
                if node.right:
                    queue.append(node.right)
            # Add the level list to the resulting list
            result.append(level_list)
        # return the final list with each level list values
        return result
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")