# Leetcode Problem 199: Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if the root node is null or no tree is given, we return []
        if root is None:
            return []
        # initialize empty output list to hold the result
        output = []
        # convert the given tree into queue
        queue = deque([root])
        # loop until we process all the nodes in tree
        while queue:
            # find the size of each level
            size = len(queue)
            # loop until we process all the nodes in each level
            for i in range(size):
                # popleft the node
                node = queue.popleft()
                
                # we need to add only the last element of the level to output list
                if i == size - 1:
                    output.append(node.val)
                # if there are any nodes to the left, add them to queue
                if node.left:
                    queue.append(node.left)
                # if there are any nodes to the right, add them to queue
                if node.right:
                    queue.append(node.right)
        # finally, return the output
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")