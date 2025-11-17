# Leetcode Problem 2415: Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the given root is none or no root, we return empty list
        if not root or root is None:
            return []
        # convert the given tree into queue
        queue = deque([root])
        # let the level be 0
        level = 0
        # loop until we process all the nodes in queue
        while queue:
            # initialize the level list
            level_list = []
            # find the length of the queue
            level_size = len(queue)
            # loop until we process all the level nodes
            for i in range(level_size):
                node = queue.popleft()
                # append the node instead of value
                level_list.append(node)

                # add the left nodes to the queue
                if node.left:
                    queue.append(node.left)
                # add the right nodes to the queue
                if node.right:
                    queue.append(node.right)
            # if the level is odd, we need to reverse them, using two pointers approach
            if level % 2 == 1:
                left = 0
                right = len(level_list) - 1
                while left < right:
                    level_list[left].val, level_list[right].val = (level_list[right].val, level_list[left].val)
                    left += 1
                    right -= 1
            level += 1
        # finally, return the root of the tree
        return root
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")