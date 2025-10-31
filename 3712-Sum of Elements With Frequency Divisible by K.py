# Leetcode Problem 3712: Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/description/
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # initialize an empty hash_map to get frequency of each number in nums list
        hash_map = {}
        # initialize the sum to 0
        sum = 0
        # find the frequency of each number in the nums list
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # loop through each num and it's count from the hash_map
        for num, count in hash_map.items():
            # check if the frequency of each number is divisible by k and add that sum
            if count % k == 0:
                sum += (num * count)
        # return the sum at the end
        return sum

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")