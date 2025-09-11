# Leetcode Problem 728: Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # initialize an empty result list to store the values
        result = []
        # loop through the given range
        for i in range(left, right+1):
            # check if the number is self dividing or not
            if self.self_dividing(i):
                # append that number to result list
                result.append(i)
        # return the result
        return result
    
    # helper function to check whether the number is self dividing or not
    def self_dividing(self, n: int) -> bool:
        # assing that number to temp
        temp = n
        # checking each digit in num is self dividing or not
        while n > 0:
            remainder = n % 10
            if remainder == 0 or temp % remainder != 0:
                return False
            n = n // 10
        return True
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")