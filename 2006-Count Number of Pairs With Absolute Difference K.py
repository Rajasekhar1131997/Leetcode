# Leetcode Problem 2006: Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # initialize the count to 0
        count = 0
        # outer loop covering all the elements from index 0
        for i in range(len(nums)):
            # inner loop starting from the index 1
            for j in range(i+1, len(nums)):
                # check the given condition and if it satisfies, we increase the count
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        # return the count
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")