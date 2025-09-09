# Leetcode Problem 2798: Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through each value in hours list
        for i in range(len(hours)):
            # check if the employee worked for targeted number of hours or not
            if hours[i] >= target:
                count += 1
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")