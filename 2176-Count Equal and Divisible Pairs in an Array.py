# Leetcode Problem 2176: Count Equal and Divisible Pairs in an Array
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through each element in nums
        for i in range(len(nums)):
            # inner loop to process each element starting with i
            for j in range(i, len(nums)):
                # check conditions and if satisfied, increase the count by 1
                if i < j:
                    if nums[i] == nums[j] and (i * j) % k == 0:
                        count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")