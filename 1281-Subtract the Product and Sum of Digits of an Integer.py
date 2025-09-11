# Leetcode Problem 1281: Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # initialize the product to 1 and sum to 0
        product = 1
        sum = 0
        # get each digit from n
        while n > 0:
            remainder = n % 10
            product *= remainder
            sum += remainder
            n = n // 10
        # return the difference of product and sum
        return product - sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")