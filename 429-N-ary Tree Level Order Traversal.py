# Leetcode Problem 429: N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # if the tree is empty or no tree is given, we return empty list
        if not root or root is None:
            return []
        # convert the given tree into queue
        queue = deque([root])
        # initialize an empty output list
        output = []
        # loop until we process all the values in queue
        while queue:
            # initialize an empty list to add values of each row
            level_list = []
            # find the len of each level
            level_size = len(queue)
            # loop until we process all nodes in each level
            for i in range(level_size):
                node = queue.popleft()
                level_list.append(node.val)

                # if there are childre, we add them to queue. since node.children adds them as a list, we use for loop to add each child into the queue
                if node.children:
                    for child in node.children:
                        queue.append(child)
            # append the level list to output
            output.append(level_list)
        # finally, return the output list
        return output
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")