# Leetcode Problem 2496: Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # intialize an empty result list
        result = []
        # loop through each string in strs list
        for string in strs:
            # check if the current string is all digits or not
            if string.isdigit():
                # if yes, convert the string into int and add that to result
                result.append(int(string))
            # else, we add the len of string to result list
            else:
                result.append(len(string))
        # we have to return the max element of the result list
        return max(result)

print("Time Complexity: O(N * K) => O(N)")
print("Space Complexity: O(N)")