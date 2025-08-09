# Leetcode Problem 2460: Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array/description/
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Initialize two pointers for adjacent element comparison
        left = 0
        right = 1
        n = len(nums)  # Store the length of the array

        # First pass: Apply the doubling operation
        while right < n:
            # If two adjacent elements are equal, double the first and set the second to 0
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
            # Move both pointers forward
            left += 1
            right += 1

        # Second pass: Move all non-zero elements to the front
        write = 0  # Position where the next non-zero element will be placed
        for read in range(n):
            # If the current element is not zero, move it to the 'write' position
            if nums[read] != 0:
                nums[write] = nums[read]
                # If we moved an element from a different position, set the old position to 0
                if write != read:
                    nums[read] = 0
                # Move the write pointer forward
                write += 1

        # Return the modified array
        return nums

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")