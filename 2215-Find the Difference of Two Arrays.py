# Leetcode Problem 2215: Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # we can find the difference of two arrays using sets and lists
        diff1 = list(set(nums1) - set(nums2))
        diff2 = list(set(nums2) - set(nums1))
        # return the difference of arrays in lists
        return [diff1, diff2]

print("Time Complexity: O(N1 + N2)")
print("Space Complexity: O(N1 + N2)")