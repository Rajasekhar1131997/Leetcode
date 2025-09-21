# Leetcode Problem 3536: Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/description/
class Solution:
    def maxProduct(self, n: int) -> int:
        # initialize empty result list
        result = []
        # add each digit into list
        while(n>0):
            remainder = n % 10
            result.append(remainder)
            n = n // 10
        # sort the result list in descending order
        result.sort(reverse=True)
        # return the product of first and second number from the list
        return result[0] * result[1]

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")

# We can solve this problem using another approach
class Solution:
    def maxProduct(self, n: int) -> int:
        # initialize the max1 and max2 variables to -1
        max1, max2 = -1, -1
        # we keep changing max1 and max2 for every digit
        while n>0:
            digit = n % 10
            n //= 10

            # if the current digit is greater than max1, we assign the max1, max2 to digit and max1
            if digit > max1:
                max1, max2 = digit, max1
            # else if digit > max2 we assign max2 to digit
            elif digit > max2:
                max2 = digit
        # finally, return the product of max1 and max2
        return max1 * max2

print("Time Complexity: O(d)")
print("Space Complexity: O(1)")