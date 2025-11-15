# Leetcode Problem 1305: All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # initialize an empty output list
        output = []
        # helper function to traverse the tree in depth first search algo.
        def dfs(node):
            # if the node is empty, we exit the helper function
            if not node:
                return
            # traverse the left node of the tree
            dfs(node.left)
            # append the current node value to the output
            output.append(node.val)
            # traverse the right node of the tree
            dfs(node.right)
        # call the helper function with root1 tree node
        dfs(root1)
        # call the helper function with root2 tree node
        dfs(root2)
        # sort the output list
        output.sort()
        # finally, return the output list
        return output

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")