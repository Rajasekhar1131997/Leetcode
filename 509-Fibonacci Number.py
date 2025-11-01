# Leetcode Problem 509: Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def fib(self, n: int) -> int:
        # base case, if the given number is less than or equal to 1, return n
        if n <= 1:
            return n
        # initialize the variables a, b to 0 and 1
        a, b = 0, 1
        # loop through 2 to n+1(until n)
        for _ in range(2, n+1):
            # assign b value to a and a+b value to b
            a, b = b, a + b
        # finally, return the b value which hold the result
        return b

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")

# we can also solve this problem recursively
class Solution:
    def fib(self, n: int) -> int:
        # base case, if the given number is less than or equal to 1, return n
        if n <= 1:
            return n
        # call the function recursively with n-1 and n-2
        return self.fib(n-1) + self.fib(n-2)

print("Time Complexity: O(2^n)")
print("Space Complexity: O(N)")