# Leetcode Problem 2578: Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/description/
class Solution:
    def splitNum(self, num: int) -> int:
        # sort the given number into list after converting into string
        digits = sorted(str(num))
        # initialize an empty num1 and num2 strings
        num1 = num2 = ""
        # loop through each index and digit in digits list
        for i, d in enumerate(digits):
            # add each digit simultaneously to num1 and num2
            if i % 2 == 0:
                num1 += d
            else:
                num2 += d
        # return the sum of both integers
        return int(num1) + int(num2)

print("Time Complexity: O(d logd), O(N logN) interms of N")
print("Space Complexity: O(N)")