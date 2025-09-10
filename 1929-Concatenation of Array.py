# Leetcode Problem 1929: Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/description/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we can simply concatenate the given list by adding them
        return nums + nums

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")