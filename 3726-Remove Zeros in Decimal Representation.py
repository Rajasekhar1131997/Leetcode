# Leetcode Problem 3726: Remove Zeros in Decimal Representation
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/

class Solution:
    def removeZeros(self, n: int) -> int:
        # initialize an empty string
        new_str = ""
        # convert the given int to string to iterate each character
        string = str(n)
        # loop through each character in the string
        for char in string:
            # if the char is not 0, we append that character to new string
            if char != '0':
                new_str += char
            # else, continue
            continue
        # finally, return the new string by converting it into int
        return int(new_str)

print("Time Complexity: O(logN)")
print("Space Complexity: O(logN)")