# Leetcode Problem 2595: Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/description/
from typing import List
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # using format, we convert the given number into binary and also sliced it since the bits are indexed from right to left in the binary representation of a number
        binary = format(n, "b")[::-1]
        # initializing even and odd count to 0
        even_count = odd_count = 0
        # loop through each bit/char in binary number
        for index, char in enumerate(binary):
            # if the bit is 1
            if char == '1':
                # if it's divisible by 2, we increase the even count
                if index % 2 == 0:
                    even_count += 1
                # if it's not divisible by 2, we increase the odd count
                else:
                    odd_count += 1
        # return the even and odd count
        return [even_count, odd_count]

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")