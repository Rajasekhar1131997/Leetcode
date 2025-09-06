# Leetcode Problem 412: Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/description/
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # initialize an empty result list to store the result
        result = []
        # loop through 1 to n
        for i in range(1, n+1):
            # check if i is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # check if i is divisible by 3
            elif i % 3 == 0:
                result.append("Fizz")
            # check if i is divisible by 5
            elif i % 5 == 0:
                result.append("Buzz")
            # else, we simply add that value as string to result
            else:
                result.append(str(i))
        # return result list at the end
        return result
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")