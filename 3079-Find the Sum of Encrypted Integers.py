# Leetcode Problem 3079: Find the Sum of Encrypted Integers
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        # initialize the sum to 0
        summ = 0
        # loop through each number in nums list
        for num in nums:
            # compute the summ by calling each number from nums list by calling helper function
            summ += self.encrypt(num)
        # return the summ
        return summ
    
    # helper function to convert the given number into maximum number
    def encrypt(self, x: int) -> int:
        # find the maximum number from the given number
        max_digit = max(str(x))
        # initialize the result to 0 and place to 1
        result = 0
        place = 1
        # loop until the number is greater than 0
        while x > 0:
            # compute the result
            result += int(max_digit) * place
            # for every iteration multiply with 10 and also decrease the original number
            place *= 10
            x //= 10
        # return the maximum number
        return result

print("Time Complexity: O(N * D)")
print("Space Complexity: O(1)")