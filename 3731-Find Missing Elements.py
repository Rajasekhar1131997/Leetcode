# Leetcode Problem 3731: Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/description/
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # initialize an empty list to store the missing values in the given range
        missing = []
        # find the min value from nums list
        min_value = min(nums)
        # find the max value from nums list
        max_value = max(nums)
        # conver the list to set, so that we can reduce the time complexity by searching over the set
        nums_set = set(nums)
        # loop through the min and max range
        for i in range(min_value, max_value+1):
            # check if that value is present in the nums_set list or not
            if i not in nums_set:
                # if it's missing add that value to missing list
                missing.append(i)
        # finally, return the missing elements from the nums list
        return missing

print("Time Complexity: O(N+r) => O(N)")
print("Space Complexity: O(N)")