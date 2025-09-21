# Leetcode Problem 3683: Earliest Time to Finish One Task
# https://leetcode.com/problems/earliest-time-to-finish-one-task/description/
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        # initialize the min time to infinity
        min_time = float('inf')
        # for every start, finish time in tasks
        for start, finish in tasks:
            # compute the time taken to finish the task
            time_taken = start+finish
            # find the minimum time taken by the tasks
            min_time = min(min_time, time_taken)
        # return the minimum taken as requested
        return min_time

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")