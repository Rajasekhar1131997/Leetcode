# Leetcode Problem 2951: Find the Peaks
# https://leetcode.com/problems/find-the-peaks/description/
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # initialize an empty list to return the indices of peaks
        result = []
        # loop through index 1 to the last but one element
        for i in range(1, len(mountain)-1):
            # check the given condition, where the peak is strictly greater than their neighboring elements, if yes, we append that index to result list
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                result.append(i)
        # return the result list at the end
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")