# Leetcode Problem 2899: Last Visited Integers
# https://leetcode.com/problems/last-visited-integers/description/
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        # initialize two empty arrays seen and ans
        seen = []
        ans = []
        # initialize the variable k to 0
        k = 0
        # loop through each number in nums
        for i in range(len(nums)):
            # if the current number is positive, we prepend that number to seen array
            if nums[i] > 0:
                seen.insert(0, nums[i])
                # we also reset the k value to 0 everytime we seen a positive number
                k = 0
            # if the current number is -1, we check if the k value is greater than or equal to len(seen) array, if yes, we append -1 else, we append the first element from seen array
            if nums[i] == -1:
                if k >= len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k])
                # we also keep increment the k value by 1
                k += 1
        # finally, return the ans array
        return ans

print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")