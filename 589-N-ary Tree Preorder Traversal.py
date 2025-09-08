# Leetcode Problem 589: N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
from typing import Optional, List
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # if there is no root, we return empty list
        if not root:
            return []
        # initialize empty list to return the output list
        values = []
        # using dfs helper function
        def dfs(node):
            # if the given node is empty, we return/exit the function
            if not node:
                return
            # since, its preorder, we add the root node first
            values.append(node.val)
            # traversing the tree for child nodes
            for child in node.children:
                # calling each child node
                dfs(child)
        # calling the helper function with root node
        dfs(root)
        # finally, return the preorder values list
        return values

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")