# Leetcode Problem 338: Counting Bits
# https://leetcode.com/problems/counting-bits/description/
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # initialize an empty list to store the result
        result = []
        # loop until we reach the n value
        for i in range(n+1):
            # using the helper function to get the number of n's for each digit
            ones = self.checkOnes(i)
            # append the outcome to the result list
            result.append(ones)
        # return the result
        return result
    
    # helper function to count the number of 1's in each digit
    def checkOnes(self, i: int) -> int:
        # initialize a variable to keep count of 1's
        num_of_ones = 0
        # loop until the i value is greater than 0
        while i > 0:
            # using % operator get the last digit
            digit = i % 2
            # add that digit to the number of ones variable
            num_of_ones += digit
            # decrease the i value 
            i = i // 2
        # return the number of ones for each digit
        return num_of_ones

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")

# Solving this problem using Bit Manipulation
class Solution:
    def countBits(self, n: int) -> List[int]:
        # initialize the result list with 0's of size n+1
        result = [0] * (n+1)
        # for each digit starting from 1 to n+1 (n inclusive)
        for i in range(1, n+1):
            # doing the bit manipluation
            # shifting the i value to the right by 1 and adding it with (i & 1)
            result[i] = result[i >> 1] + (i & 1)
        # returning the result
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")