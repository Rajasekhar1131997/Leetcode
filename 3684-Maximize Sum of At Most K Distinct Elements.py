# Leetcode Problem 3684: Maximize Sum of At Most K Distinct Elements
# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/description/
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # initialize an empty result list
        result = []
        # sort the given nums list in descending order
        nums.sort(reverse = True)
        # loop through each num in nums list
        for num in nums:
            # if num not in result, we append that num to the result
            if num not in result:
                result.append(num)
            # we also check if the length of result list is equal to integer k and break it
            if len(result) == k:
                break
        # return the result list which holds the numbers in strictly descending order
        return result

print("Time Complexity: O(N logN)")
print("Space Complexity: O(K), since it depends on given integer")