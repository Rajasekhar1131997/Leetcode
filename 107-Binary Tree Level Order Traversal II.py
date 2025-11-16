# Leetcode Problem 107: Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if there is no root or empty empty, we return []
        if not root:
            return []
        # initialize the output list to store the result
        output = []
        # converting the given tree into queue
        queue = deque([root])
        # loop until we process all nodes in queue
        while queue:
            # initialize an empty level list to hold node values of each level
            level_list = []
            # find the size of each level
            level_size = len(queue)
            # loop through all values in each level
            for _ in range(level_size):
                # popleft the value from queue and add it to level list
                node = queue.popleft()
                level_list.append(node.val)

                # if there are any left nodes, we add them to queue
                if node.left:
                    queue.append(node.left)
                # if there are any right nodes, we add them to queue
                if node.right:
                    queue.append(node.right)
            # add the level list to output
            output.append(level_list)
        # we need to reverse the entire list as we need to return the bottom-up level order of nodes
        output.reverse()
        # return the output list
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")