# Leetcode Problem 590: N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
from typing import Optional, List
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # if the tree is empty or no root node, we return empty list
        if not root:
            return []
        # initialize an empty values list to hold the postorder list
        values = []
        # helper function to traverse the tree in dfs
        def dfs(node):
            # if there is no node or node is empty, we reture/exit the function
            if not node:
                return
            # traverse the tree for every child node
            for child in node.children:
                dfs(child)
            # append the root node at the end, since it's postorder traversal
            values.append(node.val)
        # calling the helper function with root node
        dfs(root)
        # return the values list holding postorder traversal values
        return values

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")