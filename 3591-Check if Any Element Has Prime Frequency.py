# Leetcode Problem 3591: Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # initialize an empty hash map
        hash_map = {}
        # logic to get frequency of each element
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # now loop through each value in hash map values
        for count in hash_map.values():
            # if any of the frequency value is prime, we return True, otherwise False
            if self.isprime(count):
                return True
        return False
    
    # helper function to check whether number is prime or not
    def isprime(self, n: int) -> bool:
        # if the value is 1, return False
        if n == 1: return False
        # if the value is 2 or 3, we return True, since they are prime numbers
        if n == 2 or n == 3: return True
        # if the value is either even or divisible by 3, return False
        if n % 2 == 0 or n % 3 == 0:
            return False
        # starting from 5, below is the logic to find whether it's a prime number or not
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True

print("Time Complexity: O(N * sqrt(N)) -> O(N)")
print("Space Complexity: O(N)")