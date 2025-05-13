/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// Approach: Binary Search

// Leetcode: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null; // Edge case
        return constructTreefromArray(nums, 0, nums.length-1); // Recursive function to construct the tree
    }
    public TreeNode constructTreefromArray(int []nums, int left, int right){ // Recursive function to construct the tree
        if(left>right) return null; // Base case
        int mid = (left+right)/2; // Find the middle element
        TreeNode node = new TreeNode(nums[mid]); // Create a new node with the middle element
        node.left = constructTreefromArray(nums, left, mid-1); // Recursively construct the left subtree
        node.right = constructTreefromArray(nums,mid+1, right); // Recursively construct the right subtree
        return node; // Return the constructed node
    }
}