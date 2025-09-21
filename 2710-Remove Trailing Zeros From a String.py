# Leetcode Problem 2710: Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # we can use rstrip to remove the unwanted zeros from the string
        num = num.rstrip("0")
        # return the number again as a string
        return num
        