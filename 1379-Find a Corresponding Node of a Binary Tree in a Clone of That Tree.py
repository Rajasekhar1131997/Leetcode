# Leetcode Problem 1379: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # convert the given original tree and cloned trees into queue
        original_tree = deque([original])
        cloned_tree = deque([cloned])

        # loop until we process all the nodes in both the trees
        while original_tree:
            o = original_tree.popleft()
            c = cloned_tree.popleft()

            # if the popped node is equal to the target node, we return the reference of the cloned tree
            if o == target:
                return c

            # we also need to add the nodes to the left and right of the original and cloned trees to the queues
            if o.left:
                original_tree.append(o.left)
                cloned_tree.append(c.left)
            if o.right:
                original_tree.append(o.right)
                cloned_tree.append(c.right)
        # if there is no target node in the original or clone, we return None
        return None

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")