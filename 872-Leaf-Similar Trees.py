# Leetcode Problem 872: Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # check with the roots of the trees
        return self.dfs(root1) == self.dfs(root2)

    # using depth first search method to process each tree
    def dfs(self, node:Optional[TreeNode]) -> List[int]:
        # initialize an empty result to hold the result
        result = []
        # if the node is empty or no tree, we return empty list
        if not node:
            return []
        # if there is no childre, we add that to the list
        if not node.left and not node.right:
            return [node.val]
        # check the left and right child of the tree
        return self.dfs(node.left) + self.dfs(node.right)
    
print("Time Complexity: O(N + M)")
print("Space Complexity: O(H), where H is the height of the tree")