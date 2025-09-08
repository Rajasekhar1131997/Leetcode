# Leetcode Problem 3131: Find the Integer Added to Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # sort the numbers from nums1 list
        nums1.sort()
        # sort the numbers from nums2 list
        nums2.sort()
        # By subtracting the mininum number from nums2 and nums1, we get the x
        x = min(nums2) - min(nums1)
        # return x value
        return x

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")