# Leetcode Problem 653: Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # convert the given tree into queue
        queue = deque([root])
        # initialize an empty output list to hold all the node values
        output = []
        # loop until we process all the nodes in tree
        while queue:
            # find the size of the queue
            size = len(queue)
            # loop until we process all the nodes in each level
            for _ in range(size):
                # pop the left nodes from the queue
                node = queue.popleft()
                # append each node value to output list
                output.append(node.val)

                # if there are any nodes to the left, append them to the queue
                if node.left:
                    queue.append(node.left)
                # if there are any nodes to the right, append them to the queue
                if node.right:
                    queue.append(node.right)
        # initialze an empty hash map
        hash_map = {}
        # loop through the list using enumerate
        for i, value in enumerate(output):
            # find the difference
            difference = k - value
            # check if that difference value is present in hashmap or not, if yes, return True
            if difference in hash_map:
                return True
            # we also need to insert that value to hashmap
            hash_map[value] = i
        # return false, if there any two such elements in BST, which produces sum equal to k
        return False
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")