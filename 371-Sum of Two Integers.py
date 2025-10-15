# Leetcode Problem 371: Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Create a 32-bit mask (all 1's) to simulate 32-bit integer overflow behavior
        # because Python integers can grow arbitrarily large.
        mask = 0xFFFFFFFF
        # Define the maximum positive integer for a signed 32-bit number (2^31 - 1)
        maxInt = 2**31 - 1
        # Repeat the addition process until there is no carry left
        while b != 0:
            # XOR operation gives the sum of bits without considering the carry
            s = (a ^ b) & mask
            # AND operation followed by a left shift gives the carry bits
            c = (a & b) & mask
            # Assign the partial sum to a
            a = s
            # Carry is shifted left by one because it affects the next higher bit
            b = c << 1   
        # If the result is within the range of positive 32-bit integers, return it directly
        # Otherwise, convert it to a negative number using bit inversion (~) and masking
        return a if a <= maxInt else ~(a ^ mask)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

# We can use the below method as well to solve this problem
return int(math.log(math.exp(a) * math.exp(b)))

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")