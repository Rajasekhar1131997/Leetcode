# Leetcode Problem 1619: Mean of Array After Removing Some Elements
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # find the length of the given arr
        n = len(arr)
        # sort the array
        arr.sort()
        # remove the smallest and largest 5% of the array
        cut = n // 20
        # assign the trimmed array to variable
        trimmed = arr[cut:n-cut]
        # return the mean
        return sum(trimmed) / len(trimmed)

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")