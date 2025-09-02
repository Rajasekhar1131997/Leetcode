# Leetcode Problem 2824: Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through each value in nums
        for i in range(len(nums)):
            # loop through each value in nums
            for j in range(len(nums)):
                # need to satisfy the condition 0<=i<j<n
                if i < j:
                    # need to satisfy this condition as well
                    if nums[i] + nums[j] < target:
                        # we increment the count by 1
                        count += 1
        # return count
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")

# This approach will take O(N logN) time complexity since, we are sorting the array and applying two pointers
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # First, sort the array so we can apply the two-pointer technique.
        # Sorting ensures that as we move pointers, we can reason about sums in order.
        nums.sort()  

        # Initialize two pointers:
        # i starts from the beginning (smallest number),
        # j starts from the end (largest number).
        i, j = 0, len(nums) - 1

        # Variable to keep track of the total number of valid pairs found.
        count = 0

        # Continue while the two pointers do not cross.
        while i < j:
            # Case 1: if the sum of nums[i] and nums[j] is less than target...
            if nums[i] + nums[j] < target:
                # Then ALL pairs (nums[i], nums[k]) where i < k ≤ j are valid.
                # This is because nums[k] ≤ nums[j] (since array is sorted),
                # so nums[i] + nums[k] will also be < target.
                count += (j - i)  # Add the number of such pairs at once.

                # Move i forward to check the next possible left element.
                i += 1
            else:
                # Case 2: if nums[i] + nums[j] is too large (>= target),
                # then we need a smaller sum → move j leftwards.
                j -= 1

        # Return the total count of valid pairs.
        return count

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")