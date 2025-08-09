# Leetcode Problem 1089: Duplicate Zeros
# https://leetcode.com/problems/duplicate-zeros/description/
from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # find the length of the given arry
        n = len(arr)
        # initialize the variable zero count to find zeros in the array
        zero_count = 0
        # logic to find the number of zeros in array
        for i in range(n):
            if arr[i] == 0:
                zero_count += 1
        # traversing the array from the end
        for i in range(n-1, -1, -1):
            # If the element's new position after duplicating zeros is still within bounds
            if i + zeros < n:
                # Move the current element to its new position
                arr[i + zeros] = arr[i]

            # If the current element is zero, we need to account for duplication
            if arr[i] == 0:
                # One zero has been processed, reduce the count
                zeros -= 1
                # After reducing, if the new duplicated zero is within bounds, insert it
                if i + zeros < n:
                    arr[i + zeros] = 0

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")