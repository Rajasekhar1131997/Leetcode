# Leetcode Problem 105: Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either traversal list is empty, no tree can be formed
        if not preorder or not inorder:
            return None
        # The first element in preorder list is always the root of the current subtree
        root = TreeNode(preorder[0])
        # Find the index of this root value in the inorder list
        # This divides the inorder list into left and right subtrees
        mid = inorder.index(preorder[0])
        # Recursively build the left subtree:
        # - preorder[1:mid+1] contains the nodes belonging to the left subtree (after the root)
        # - inorder[:mid] contains the left subtree nodes as per inorder sequence
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # Recursively build the right subtree:
        # - preorder[mid+1:] contains nodes for the right subtree
        # - inorder[mid+1:] contains the right subtree nodes as per inorder sequence
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # Return the constructed root node (which links to its left and right subtrees)
        return root

print("Time Complexity: O(N^2) as the inorder.index will be O(n) recursive call")
print("Space Complexity: O(N) due to recursive call stack")