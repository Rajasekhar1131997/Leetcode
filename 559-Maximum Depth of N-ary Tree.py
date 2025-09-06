# Leetcode Problem 559: Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
from typing import Optional, List
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # if there is no root node, we return 0
        if not root:
            return 0
        # if there is a root node and no children present, we return 1
        if not root.children:
            return 1
        # finally, we traverse all the nodes in the tree, +1 is for root is for root of the node
        return 1 + max(self.maxDepth(child) for child in root.children)

print("Time Complexity: O(N)")
print("Space Complexity: O(H), where H is the height of the tree")