# Leetcode Problem 2169: Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/description/
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # recursive function to get count
        def getcount(num1, num2, count):
            # if any of the numbers is 0, we return count
            if num1 == 0 or num2 == 0:
                return count
            # if the num1 is greater than or equal to num2, call the recursive function
            if num1 >= num2:
                num1 = num1 - num2
                return getcount(num1, num2, count+1)
            # if the num2 is greater than or equal to num1, call the recursive function
            else:
                num2 = num2 - num1
                return getcount(num1, num2, count+1)
        # call the recursive function with given num1 and num2 with 0 count
        return getcount(num1, num2, 0)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")


# We can solve this problem using iterative approach
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # initialize the count to 0
        count = 0
        # loop until the num1 and num2 are not zeroes
        while num1 and num2:
            # if num1 >= num2, subtract num1 - num2
            if num1 >= num2:
                num1 = num1 - num2
            # if num2 >= num1, subtract num2 - num1
            else:
                num2 = num2 - num1
            # increase the count by 1
            count += 1
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")