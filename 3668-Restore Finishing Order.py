# Leetcode Problem 3668: Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/
from typing import List
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # initialize an empty result list to hold the output values
        result = []
        # for every number in order list
        for num in order:
            # if the number is present in friends, we append that value to result
            if num in friends:
                result.append(num)
        # return the result list
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")