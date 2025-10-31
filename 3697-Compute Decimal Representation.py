# Leetcode Problem 3697: Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/description/
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # initialize an empty result list
        result = []
        # initialize the place as 1, later we multiply with base 10 for every iteration
        place = 1
        # loop until n value is greater than 0
        while(n>0):
            # get the end digit from the given number
            temp = n % 10
            # find the value of that number with respect to base-10
            value = temp * place
            # if that value is 0, we skip adding that value to our result, else we continue
            if value != 0:
                result.append(value)
            # we also need to change the place value multiplying it by 10
            place *= 10
            # divide the n by 10, since the last digit is processed.
            n = n // 10
        # we return the result list in desc order, since the values are processed from right to left
        return result[::-1]

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")