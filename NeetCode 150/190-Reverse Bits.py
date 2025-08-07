# Leetcode Problem 190: Reverse Bits
# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        # if the given number is 0, return 0
        if n == 0:
            return 0
        # initialize a variable reversed_n which will hold the reversed number
        reversed_n = 0
        # loop until all the 32 bits are processed
        for i in range(32):
            # we need to move the reversed_n to left by 1 bit to accomodate the next bit
            reversed_n = reversed_n << 1
            # Trying to last bit from 32 bits
            bit = n & 1
            # now, adding that bit to the reversed_n
            reversed_n = reversed_n | bit
            # we need to move the n to right side by 1 bit
            n = n >> 1
        # return the reversed number
        return reversed_n

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")