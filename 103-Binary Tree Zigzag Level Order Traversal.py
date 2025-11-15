# Leetcode Problem 103: Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if the root or no root node is given, we return empty list
        if root is None:
            return []
        # initializing empty output list to store result
        output = []
        # convert the given root into queue
        queue = deque([root])
        # let left to right be true
        left_to_right = True

        # loop until we process all the nodes in the queue
        while queue:
            # since, we need to append the node values for each leve, we initialize an empty list
            level_list = []
            # find the length of each level
            level_length = len(queue)
            # loop until we process each node for each level
            for i in range(level_length):
                # popleft the node from queue
                node = queue.popleft()
                # append that popped value to level list
                level_list.append(node.val)
                # check if there are any left nodes and add them to queue
                if node.left:
                    queue.append(node.left)
                # check if there are any right nodes and add them to queue
                if node.right:
                    queue.append(node.right)
            # if not left to right, we need to reverse the list
            if not left_to_right:
                level_list.reverse()
            # we need to add that level list to output list
            output.append(level_list)
            # alternate the left to right variable simultaneously
            left_to_right = not left_to_right
        # finally, return the output
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")