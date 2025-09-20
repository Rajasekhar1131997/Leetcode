# Leetcode Problem 252: Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        last_end = -1
        for Interval in intervals:
            if Interval.start < last_end:
                return False
            last_end = Interval.end
        return True

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")