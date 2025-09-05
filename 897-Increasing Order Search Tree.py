# Leetcode Problem 897: Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/description/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inorder helper function to traverse the tree and get all values
        def inorder(node):
            # if the tree is empty, we return empty list
            if not node:
                return []
            # traversing the tree inorder left nodes, root node, right nodes
            return inorder(node.left) + [node] + inorder(node.right)
        nodes = inorder(root)
# once, we get the list of nodes, we can build a new tree having no left child, with only right child
        # creating a dummy node
        dummy = TreeNode(-1)
        # pointing the dummy node to current pointer
        current = dummy
        # looping through each node in nodes list
        for node in nodes:
            # assinging the left child to none
            current.left = None
            # appening the right child to current node
            current.right = node
            # current pointer to node
            current = node
        # since, we are starting with dummy pointer, the main root will be right of the dummy
        return dummy.right
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# Solving this problem without creating a list
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inorder helper function to traverse the tree and get all values
        def inorder(node):
            # if the tree is empty, we return empty list
            if not node:
                return []
            # calling the nonlocal current pointer to function
            nonlocal current
            # traversing the tree left side
            inorder(node.left)
            # assigning the left child to none
            node.left = None
            # assigning the right child with node
            current.right = node
            # moving forward with next node
            current = node
            # traversing the right tree
            inorder(node.right)
        
        # creating a dummy TreeNode
        dummy = TreeNode(-1)
        # pointing the dummy node to current pointer
        current = dummy
        # calling the helper function with root node
        inorder(root)
        # returning the right child of dummy TreeNode
        return dummy.right

print("Time Complexity: O(N)")
print("Space Complexity: O(H), H is height of the tree")