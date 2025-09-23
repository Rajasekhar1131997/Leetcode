# Leetcode Problem 374: Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # initialize the low to 1 and high to given n number
        low = 1
        high = n
        # find the mid point based on the low and high number
        while low <= high:
            mid = (low + high) // 2
            # call the guess method to find if it is the picked number
            result = guess(mid)
            # if the result is 0, then it is the picked number
            if result == 0:
                return mid
            # if the result is 1, then the number is less than picked number
            if result == 1:
                low = mid + 1
            # if the result is -1, then the number is greater than picked number
            else:
                high = mid - 1

print("Time Complexity: O(logN)")
print("Space Complexity: O(1)")