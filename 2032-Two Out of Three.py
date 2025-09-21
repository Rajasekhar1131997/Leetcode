# Leetcode Problem 2032: Two Out of Three
# https://leetcode.com/problems/two-out-of-three/description/
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # convert all the given lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        # using set intersections to find the common elements and set union to combine the results
        return list((set1 & set2) | (set2 & set3) | (set1 & set3))

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")