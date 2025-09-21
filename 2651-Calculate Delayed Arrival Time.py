# Leetcode Problem 2651: Calculate Delayed Arrival Time
# https://leetcode.com/problems/calculate-delayed-arrival-time/description/
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # calculate the arrival time at station which is sum of arrival and delayed time
        total_time = arrivalTime + delayedTime
        # if the total time is equal to 24, we return 0, otherwise return the total time calculated
        if total_time == 24:
            return 0
        # if the any of the times is greater than 24, we simply subtract the total time from 24
        elif total_time > 24:
            total_time = total_time - 24
            return total_time
        # otherwise, we return total time
        else:
            return total_time

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")