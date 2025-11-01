# Leetcode Problem 2656: Maximum Sum With Exactly K Elements 
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # initialize the variable sum to 0
        summ = 0
        # loop until we process exactly k times
        while k != 0:
            # find the maximum element from the nums list
            m = max(nums)
            # add that value to the sum
            summ += m
            # we also need to remove that element from the nums list
            nums.remove(m)
            # need to append the value m+1 to the array
            nums.append(m+1)
            # for every operation, we decrement the k value
            k -= 1
        # return the summ at the end
        return summ

print("Time Complexity: O(N x K)")
print("Space Complexity: O(1)")