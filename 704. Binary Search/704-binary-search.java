// LeetCode 704. Binary Search
// https://leetcode.com/problems/binary-search/
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) // Check if the array is empty
            return -1;
        int left = 0; // Initialize left pointer
        int right = nums.length - 1; // Initialize right pointer
        while (left <= right) { // While the left pointer is less than or equal to the right pointer
            int mid = (left + right) / 2; // Calculate the middle index
            if (nums[mid] == target) { // If the middle element is equal to the target
                return mid; // Return the middle index
            } else if (nums[mid] > target) { // If the middle element is greater than the target
                right = mid - 1; // Move the right pointer to the left
            } else { // If the middle element is less than the target
                left = mid + 1; // Move the left pointer to the right
            }
        }
        return -1; // If the target is not found, return -1
    }
}