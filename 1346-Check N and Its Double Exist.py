# Leetcode Problem 1346: Check N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # initialize an empty set
        seen = set()
        # loop through each value in the array
        for num in arr:
            # check if the arr * 2 or (num%2==0 and num //2) is present in seen set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                # if it's available, return True
                return True
            # add that value to the set
            seen.add(num)
        # we return false, it the above case doesn't exist
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")