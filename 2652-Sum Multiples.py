# Leetcode Problem 2652: Sum Multiples
# https://leetcode.com/problems/sum-multiples/description/
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # initialize the total to 0
        total = 0
        # check the integers from the range (1, n) inclusively if they are divisible by 3, 5 or 7
        for i in range(1, n+1):
            if (i % 3) == 0 or (i % 5) == 0 or (i % 7) == 0:
                # if yes, we add that number to total
                total += i
        # return the total
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")