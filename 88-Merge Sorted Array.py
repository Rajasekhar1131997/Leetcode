# Leetcode Problem 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # let p be the combined length of m and n lists
        p = m + n - 1
        # initialize the p1 pointer to the end of nums1
        p1 = m - 1
        # initialize the p2 pointer to the end of nums2
        p2 = n - 1
        # modifying the nums1 list inplace, loop until all the values in p1 and p2 are processed.
        while (p1 >= 0 and p2 >= 0):
            # check if the value in nums1 is greater than value in nums2
            if nums1[p1] > nums2[p2]:
                # assign that value to the end of nums1 list
                nums1[p] = nums1[p1]
                # decrease the p pointer and p1 pointer
                p -= 1
                p1 -= 1
             # if the above condition doesn't satisfy, we assign the value from nums2 to nums1
            else:
                nums1[p] = nums2[p2]
                # decrease the p pointer and p2 pointer
                p -= 1
                p2 -= 1
        # if there are still any values left in nums2, we add them to the list
        while (p2 >= 0):
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

print("Time Complexity: O(M + N)")
print("Space Complexity: O(1)")