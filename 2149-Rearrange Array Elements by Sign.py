# Leetcode Problem 2149: Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # consolidate the positive numbers into positive list
        positive = [num for num in nums if num > 0]
        # consolidate the negative numbers into negative list
        negative = [num for num in nums if num < 0]
        # initialize an empty output list to hold the result
        output = []
        # let the positive and negative indexes be 0
        positive_index, negative_index = 0, 0
        # loop through the given nums list range
        for i in range(len(nums)):
            # if it's even position, we need to add the positive integer to the list
            if i % 2 == 0:
                output.append(positive[positive_index])
                # incrementing the positive index by 1
                positive_index += 1
            # if it's odd position, we need to add the negative integer to the list
            else:
                output.append(negative[negative_index])
                # incrementing the negative index by 1
                negative_index += 1
        # return the output list
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")